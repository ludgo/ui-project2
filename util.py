# copy list and swap items at indexes
def swap(arr, indexA, indexB):
	c = list(arr)
	c[indexA], c[indexB] = c[indexB], c[indexA]
	return c

# output dictionary to file
def outputFile(dic, fileName='output.txt', accessMethod='a'):
	with open(fileName, accessMethod) as f:
		for key, value in dic.items():
			f.write('{}: {}\n'.format(key, value))
		f.write('\n')

# dictionary containing uninformed search description parameters
def buildInfoDic(search_method, start_at, end_at):
	return {
		'depth' : 0,
		'end_at' : end_at,
		'explored_count' : 0,
		'queue_size_end' : 0,
		'queue_size_max' : 0,
		'meet_at' : [],
		'path' : [],
		'search_method' : search_method,
		'start_at' : start_at,
		'time_algo' : 0
	}

def numInversions(seq):
	count_inversions = 0
	length = len(seq)
	for i in range(length):
		for j in range(i+1, length):
			if not ('0' in (seq[i], seq[j])) and (seq[i] > seq[j]):
				count_inversions += 1
	return count_inversions

# check puzzle is solvable
# !! 3x3 board only
def isSolvable(initSeq, goalSeq):
	return ( (numInversions(initSeq) % 2) + (numInversions(goalSeq) % 2) ) != 1
