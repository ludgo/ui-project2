from util import swap

# search graph node
class State(object):

	UP = 'Up'
	DOWN = 'Down'
	LEFT = 'Left'
	RIGHT = 'Right'

	@staticmethod
	def setParams(m_rows, n_cols):
		State.m = m_rows
		State.n = n_cols
		State.size = m_rows * n_cols

	def __init__(self, seq, parent=None, move=None):
		# comma separated numbers of puzzle game fields
		self.seq = seq
		# reference to parent state
		self.parent = parent
		# by which move got here from parent
		self.move = move

	# return opposite direction of actual move
	def reversedMove(self):
		if self.move == State.UP:
			return State.DOWN
		if self.move == State.DOWN:
			return State.UP
		if self.move == State.LEFT:
			return State.RIGHT
		if self.move == State.RIGHT:
			return State.LEFT

	# get sequence after 'up' on board
	def up(self, blankIndex):
		pos = blankIndex + State.n
		if (pos >= 0) and (pos < State.size):
			return swap(self.seq, pos, blankIndex)
		return None

	# get sequence after 'down' on board
	def down(self, blankIndex):
		pos = blankIndex - State.n
		if (pos >= 0) and (pos < State.size):
			return swap(self.seq, pos, blankIndex)
		return None

	# get sequence after 'left' on board
	def left(self, blankIndex):
		pos = blankIndex + 1
		if (pos >= 0) and (pos < State.size) and (pos % State.n != 0):
			return swap(self.seq, pos, blankIndex)
		return None

	# get sequence after 'right' on board
	def right(self, blankIndex):
		pos = blankIndex - 1
		if (pos >= 0) and (pos < State.size) and (pos % State.n != State.n - 1):
			return swap(self.seq, pos, blankIndex)
		return None

	# create neighbour states as children with depth +1, except parent
	def findChildren(self):
		self.udlr = [None, None, None, None]
		blank = self.seq.index('0')
		if self.move != State.DOWN:
			childSeq = self.up(blank)
			if childSeq:
				self.udlr[0] = State(childSeq, self, State.UP)
		if self.move != State.UP:
			childSeq = self.down(blank)
			if childSeq:
				self.udlr[1] = State(childSeq, self, State.DOWN)
		if self.move != State.RIGHT:
			childSeq = self.left(blank)
			if childSeq:
				self.udlr[2] = State(childSeq, self, State.LEFT)
		if self.move != State.LEFT:
			childSeq = self.right(blank)
			if childSeq:
				self.udlr[3] = State(childSeq, self, State.RIGHT)

	def hashKey(self):
		return str(self.seq)

