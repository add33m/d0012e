
def insertionSort2(arr):
    n = len(arr)  # Get the length of the array
      
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
    return arr

def megesort(list, k):

    listlist = []

    # splits the list up in sublists, sorts the sublist with insertion or bsort and appends each sublist to the list of lists "listlist".
    for i in range(0, len(list), k):
        n = len(list)
        if n <= 1:
            listlist.append[i:i + k]
        else:
            tempList = list[i:i + k]
            tempList = insertionSort2(tempList)
            listlist.append(tempList)

    # outer while loop that repeats the inner merge loop until the list of lists only contains one compleate merged list.
    while (len(listlist) > 1):
    # inner while loop that merges two lists (list1 and list2) inside the list-list and then returns the merged list into the list-list
        i = 0
        while i < (len(listlist)-1):
            listlist[i] = merge(listlist[i], listlist[i+1])
            listlist.pop(i+1)
            i += 1
    # returns the first and only list left inside the list of lists, that should now contain all sorted values
    return listlist[0]

    #the merge function that uses standard merge-sort technique to merge two sorted lists into one sorted list
def merge(list1, list2):

    l = []
    i = 0
    j = 0
  
    # runs loop until we have reached the end of either list 1 or list 2
    while i < len(list1) and j < len(list2):

    # if the smallest element left in list 1 is smaller than the smallest element left in list 2, append it into the merged list.
        if list1[i] < list2[j]:
            l.append(list1[i])
            i += 1
    # if the smallest element left in list 2 is smaller than the smallest element left in list 1, append it into the merged list.
        else:
            l.append(list2[j])
            j += 1

    # append the rest of the numbers from the list that still has numbers left inside of it after te while loop has compleated.
    l += list1[i:]
    l += list2[j:]

    # returns the merged list
    return l

newList = [5,3,1,2,6,4,9,7,8,10,61,55,33,45,86,32,14,57,87,99,55,30,22,66,88]

print(newList)

print(megesort(newList, 3))