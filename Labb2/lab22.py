import math as m

def linearVersion2(arr):
    n = len(arr)  # Get the length of the array
    outputArray = [0,0,0]
    outputArray[0] = m.inf
    outputArray[1] = m.inf
    outputArray[2] = m.inf

    for j in range(0, n):
        if outputArray[0] >= arr[j]:
            outputArray[2] = outputArray[1]
            outputArray[1] = outputArray[0]
            outputArray[0] = arr[j]
        elif outputArray[1] >= arr[j]:
            outputArray[2] = outputArray[1]
            outputArray[1] = arr[j]
        elif outputArray[2] >= arr[j]:
            outputArray[2] = arr[j]
        j+= j
    return outputArray











#--------------------------------------------------------------------------------------------------------------------------------







#every time it makes 2 checks, two splits, and merges shit together
#every time it will return without splitting 3 times. Only doing 1 or 2 operations.
#n should therefore be kn*3 -      up to kn*3 - 6


def divConVersion(arr):
    n = len(arr)  # Get the length of the array
    if n == 1:
        return arr[0]
    if n == 2:
        if arr[0] <= arr[1]:
            return arr[0]
        else:
            return arr[1]
    mid1 = n//3
    mid2 = mid1*2
    a1 = divConVersion(arr[0:mid1])
    a2 = divConVersion(arr[mid1:mid2])
    a3 = divConVersion(arr[mid2:n])
    if a1 <= a2 and a1 <= a3:
        return a1
    if a2 <= a3:
        return a2
    else:
        return a3
    
# Jag skulle ju tekniskt sätt kunna göra en divide and conquer som är incremental... som merge sorten...
# Då hade jag haft tillgång till pop... vilket jag ändå inte får använda :(

def divConVersion2(arr):
    n = len(arr)  # Get the length of the array
    #Basfall
    if n == 1:
        return arr
    mid1 = n//2
    a1 = divConVersion2(arr[0:mid1])
    a2 = divConVersion2(arr[mid1:n])
    if a1 <= a2:
        return a1
    else:
        return a2



#Divconc 3????? indexproblems...

def divConVersion3(arr):
    n = len(arr)  # Get the length of the array
    #Basfall
    if n == 1:
        return arr
    mid1 = n//2
    a1 = divConVersion3(arr[0:mid1])
    a2 = divConVersion3(arr[mid1:n])
    if a1[0] <= a2[0]:
        if a1[1] <= a2[0]:
            return a1[0], a1[1]
        else:
            return a1[0], a2[0]
    else:
        if a2[1] <= a1[0]:
            return a2[0],a2[1]
        else:
            return a2[0],a1[0]






arra = [5,-20,10,8,7,2,1,13,77,65,35,3,57,87,99,88,51,32,66,666,-9,-10]
arra2 = [5,20,10,8,7,2,1,13,55,0,8,-7,-9,-11,-13]
arra3 = [5,20,10,8,7,2,1,13,55,0,8,-7,-9,-11,-13]
#print("This is the result: ", linearVersion(arra))                  #It makes (3n)-3 operations
print("This is they result ", linearVersion2(arra))
print("This is the other result: ", divConVersion(arra2))
print("This is the other result: ", divConVersion2(arra3))