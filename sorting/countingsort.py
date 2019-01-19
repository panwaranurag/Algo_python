import sys


def maximum(arr):
    l = len(arr)
    if l == 0:
        return 0
    max = - sys.maxint -1
    for i in range(l):
        if arr[i] > max:
            max = arr[i]
    return max

def sort(arr):
    max = maximum(arr)
    sorted = [0]*len(arr)
    counts = [0]*(max+1)

    for i in range(len(arr)):
        counts[arr[i]] += 1
    print counts

    for j in range(1, len(counts)):
        counts[j] += counts[j-1]
    print counts

    for i in range(len(arr)):
        sorted[counts[arr[i]]-1] = arr[i]
        counts[arr[i]] -= 1

    return sorted

if __name__ == '__main__':
    A = [3,7,6,5,5,5,34,56]
    print "A:", A
    print "Sorted array after insertion sort", sort(A)