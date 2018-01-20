# breath first search
def bfs(initState, goalSeq):

	# init queue with first state
	queue = []
	queue.append(initState)
	queue_size_max = 0 # info only

	# keep track of enqueued states - hash approach
	inqueue = {}
	inqueue[initState.hashKey()] = initState

	# checked states marker
	explored = {}

	state = None
	# while queue not empty
	while len(queue) > 0:
		queue_size_max = max(queue_size_max, len(queue)) # info only

		# pop state from queue
		state = queue.pop(0)
		inqueue[state.hashKey()] = None

		explored[state.hashKey()] = True

		if state.seq == goalSeq:
			# goal sequence found
			break

		# find neighbour states of currently observed state
		state.findChildren()
		# for all neighbours
		for child in state.udlr:
			if not child:
				# skipping parent
				continue

			try:
				if explored[child.hashKey()]:
					# already been checked
					continue
			except KeyError:
				pass
			try:
				if inqueue[child.hashKey()] == child:
					# currently enqueued
					continue
			except KeyError:
				# observed for the first time
				pass

			# enqueue state
			queue.append(child)
			inqueue[child.hashKey()] = child

	# end state, end queue size, max queue size, number of explored states
	return state, len(queue), queue_size_max, len(explored)

# bidirectional search
def bds(initState, goalState):

	# init queues with first states
	queue_1, queue_2 = [], []
	queue_1.append(initState), queue_2.append(goalState)
	queue_size_max = 0 # info only

	# keep track of enqueued states - hash approach
	inqueue_1, inqueue_2 = {}, {}
	inqueue_1[initState.hashKey()], inqueue_2[goalState.hashKey()] = initState, goalState

	# checked states marker
	explored_1, explored_2 = {}, {}

	state_1, state_2 = None, None
	# while both queues not empty
	while len(queue_1) > 0 and len(queue_2) > 0:
		queue_size_max = max(queue_size_max, len(queue_1) + len(queue_2)) # info only

		if len(queue_1) > 0:

			state_1 = queue_1.pop(0)
			inqueue_1[state_1.hashKey()] = None
			explored_1[state_1.hashKey()] = True

			if state_1.seq == goalState.seq:
				# search directions even meet at endpoint
				state_2 = goalState
				break

			try:
				if inqueue_2[state_1.hashKey()]:
					# meetpoint since currently processed state also enqueued in opposite direction search
					state_2 = inqueue_2[state_1.hashKey()]
					break
			except KeyError:
				# observed for the first time
				pass

			state_1.findChildren()
			for child in state_1.udlr:
				if not child:
					# skipping parent
					continue
				try:
					if explored_1[child.hashKey()]:
						# already been checked
						continue
				except KeyError:
					pass
				try:
					if inqueue_1[child.hashKey()] == child:
						# currently enqueued
						continue
				except KeyError:
					# observed for the first time
					pass

				# enqueue state
				queue_1.append(child)
				inqueue_1[child.hashKey()] = child

		if len(queue_2) > 0:

			state_2 = queue_2.pop(0)
			inqueue_2[state_2.hashKey()] = None
			explored_2[state_2.hashKey()] = True

			if state_2.seq == initState.seq:
				# search directions even meet at endpoint
				state_1 = initState
				break

			try:
				if inqueue_1[state_2.hashKey()]:
					# meetpoint since currently processed state also enqueued in opposite direction search
					state_1 = inqueue_1[state_2.hashKey()]
					break
			except KeyError:
				pass

			state_2.findChildren()
			for child in state_2.udlr:
				if not child:
					# skipping parent
					continue
				try:
					if explored_2[child.hashKey()]:
						# already been checked
						continue
				except KeyError:
					pass
				try:
					if inqueue_2[child.hashKey()] == child:
						# currently enqueued
						continue
				except KeyError:
					# observed for the first time
					pass

				# enqueue state
				queue_2.append(child)
				inqueue_2[child.hashKey()] = child

	# meetpoint state from init, meetpoint state from goal, end queue sizes sum, max queue sizes sum, number of explored states sum
	return state_1, state_2, len(queue_1) + len(queue_2), queue_size_max, len(explored_1) + len(explored_2)
