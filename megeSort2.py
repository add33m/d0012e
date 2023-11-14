def merge_sort2(list):
	
	k = 3
	sublist = []

	if len(list) <= 1:									# no list to sort if array has 1 or 0 elements in it.
		return list

	m = len(list)
	
	for i in range(m//k):								# the split function for splitting the list into k sublists. O(k) constant time operation
		sublist.append(list[(k*i):(k*(i+1))])			#creates the sublists
		#SORT SUBLIST HERE WITH METHOD

	print("sublist len is")
	print(len(sublist))

	i = 0
	j = 0
	l = []

	while len(l) <= 1:
		while i+1 < m//k:									#kanske behöver ändra till <= här
			l[j] = merge(sublist[i],sublist[i+1])
			i = i+2
			j = i+1
		sublist = l
		


def merge(left, right):									#merges lists together again

	l = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			l.append(left[i])
			i += 1
		else:
			l.append(right[j])
			j += 1
	while i < len(left):
		l.append(left[i])
		i += 1
	while j < len(right):
		l.append(right[j])
		j += 1

newList = [5,3,1,2,6,4,9,7,8]

print(newList)

print(merge_sort2(newList))