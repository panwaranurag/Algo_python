import math
answer = []
rec_A = []
rec_B = []
a = 0
def hunters(A,B):
    global answer, rec_A, rec_B, a, b
    na = len(A)
    nb = len(B)
    mid_a = na//2
    mid_b = nb//2
    if mid_a == 0 or mid_b == 0:
        answer.extend(max(A, B))
    print mid_a, mid_b
    i = min(A[mid_a], B[mid_b])
    j = max(A[mid_a], B[mid_b])
    #print i, j
    #a= math.log(na,2)
    #while a > 0:
    #while len(answer) <= a:
    if i == A[mid_a] and j == B[mid_b] and (mid_a != 0 or mid_b != 0):
        answer.extend(B[mid_b:])
        #a = a + len(B[mid_b:])
        rec_A = A[mid_a:]
        rec_B = B[:mid_b]
        print rec_A, rec_B
        hunters(rec_A,rec_B)
    elif i == B[mid_b] and j == A[mid_a] and (mid_a != 0 or mid_b != 0):
        answer.extend(A[mid_a:])
        #a = a + len(B[mid_a:])
        rec_A = A[:mid_a]
        rec_B = B[mid_b:]
        print rec_A, rec_B
        hunters(rec_A, rec_B)
        #a = a-1
    return answer

if __name__ == '__main__':
    A = [3,6,7,10,14,16,19,24,98]
    B = [4,8,11,17,20,21,22,25,100]
    #C = [5,9,12,13,15,18,23,26]
    print "A:", A
    print "B:", B
    #print "C:", C
    print "Sorted array after merge sort", hunters(A,B)