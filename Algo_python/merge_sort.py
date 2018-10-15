def merge_sort(A):
    n = len(A)
    if n == 1:
        return A
    mid = n//2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)
def merge(L,R):
    i = 0
    j = 0
    answer = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            answer.append(L[i])
            i = i+1
        else:
            answer.append(R[j])
            j=j+1
    if i < len(L):
        answer.extend(L[i:])
    elif j< len(R):
        answer.extend(R[j:])
    return answer

if __name__ == '__main__':
    A = [3,7,6,5,5,5,34,56]
    print "A:", A
    print "Sorted array after merge sort", merge_sort(A)