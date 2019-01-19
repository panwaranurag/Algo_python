def left(i):
    return 2*i
def right(i):
    return 2*i+1
def max_heapify(A,i): 
    global heapsize
    L=left(i)
    R=right(i)
    largest=i
    if L<heapsize and A[L]>A[i]:
        largest=L
    if R<heapsize and A[R]>A[largest]:
        largest=R
    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest)
def build_maxheap(A):
    global heapsize
    for i in range((heapsize-1)/2,-1,-1):
        max_heapify(A,i)
def heap_sort(A):
    global heapsize
    build_maxheap(A)
    for i in range(heapsize-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapsize-=1
        max_heapify(A,0)
if __name__ == '__main__':
    A = [3,7,6,5,5,5,34,56]
    heapsize = len(A)
    print "A:", A
    heap_sort(A)
    print "Sorted array after merge sort", A