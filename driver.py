import sys, time
from model import State
from algo import bfs, bds
from util import outputFile, buildInfoDic, isSolvable

# process args like
# <rows> <cols> <init-state-comma-separated-nums> <goal-state-comma-separated-nums>
def initArgs():
	try:
		assert(len(sys.argv) == 5)

		M = int(sys.argv[1])
		assert(M > 0)
		N = int(sys.argv[2])
		assert(N > 0)
		size = M*N
		
		initSeq = sys.argv[3].split(',')
		assert(len(initSeq) == size)
		for x in range(size):
			assert(str(x) in initSeq)
		goalSeq = sys.argv[4].split(',')
		assert(len(goalSeq) == size)
		for x in range(size):
			assert(str(x) in goalSeq)
	except:
		print('Bad args')
		sys.exit(1)
	
	if M >= 3 and N > 3 or M > 3 and N >= 3:
		try:
			assert(isSolvable(initSeq, goalSeq))
		except:
			print('Not solvable')
			sys.exit(1)

	return M, N, initSeq, goalSeq

# run breath first search algorithm and output corresponding characteristics
def run_bfs(initState, goalSeq):
	dic_bfs = buildInfoDic('bfs', initSeq, goalSeq)

	start_time = time.time()
	bottom_bfs, dic_bfs['queue_size_end'], dic_bfs['queue_size_max'], dic_bfs['explored_count'] = bfs(initState, goalSeq)
	dic_bfs['time_algo'] = str(round(time.time() - start_time, 8))

	dic_bfs['meet_at'] = None

	# get full path by getting backwards to init
	while bottom_bfs:
		if bottom_bfs.move:
			dic_bfs['path'].insert(0, bottom_bfs.move)
		bottom_bfs = bottom_bfs.parent

	dic_bfs['depth'] = len(dic_bfs['path'])

	outputFile(dic_bfs)
	return dic_bfs

# run bidirectional search algorithm and output corresponding characteristics
def run_bds(initState, goalState):
	dic_bds = buildInfoDic('bds', initSeq, goalSeq)

	start_time = time.time()
	bottom_bds_1, bottom_bds_2, dic_bds['queue_size_end'], dic_bds['queue_size_max'], dic_bds['explored_count'] = bds(initState, goalState)
	dic_bds['time_algo'] = str(round(time.time() - start_time, 8))

	dic_bds['meet_at'] = bottom_bds_1.seq

	# get full path by getting backwards both states and putting it alltogether
	while bottom_bds_1:
		if bottom_bds_1.move:
			dic_bds['path'].insert(0, bottom_bds_1.move)
		bottom_bds_1 = bottom_bds_1.parent
	while bottom_bds_2:
		if bottom_bds_2.move:
			dic_bds['path'].append(bottom_bds_2.reversedMove())
		bottom_bds_2 = bottom_bds_2.parent

	dic_bds['depth'] = len(dic_bds['path'])

	outputFile(dic_bds)
	return dic_bds


# find out params
M, N, initSeq, goalSeq = initArgs()

# setup board
State.setParams(M, N)

# init states
initState = State(initSeq)
goalState = State(goalSeq)

# run algorithms
if M + N < 7:
	dic_bfs = run_bfs(initState, goalSeq)
	dic_bds = run_bds(initState, goalState)

	# both paths should be equally long
	assert(dic_bfs['depth'] == dic_bds['depth'])
else:
	dic_bds = run_bds(initState, goalState)
