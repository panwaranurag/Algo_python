import math
answer = []
rec_A = []
rec_B = []
rec_C = []
a = 0
def hunters(A,B,C, length):
    global answer, rec_A, rec_B,rec_C, a, b
    while len(A) == 1 or len(B) == 1 or len(C) == 1:
        mergelist = A + B + C
        mergelist.sort()
        #mid_merge = len(mergelist)//2
        remaining = length - len(answer)
        #print mid_merge
        answer.extend(mergelist[-remaining:])
        return answer 
        break
    na = len(A)
    nb = len(B)
    nc = len(C)
    mid_a = na//2
    mid_b = nb//2
    mid_c = nc//2
    '''while len(A) == 2 or len(B) == 2 or len(C) == 2:
        break
    if len(A) == 1 and len(B) == 1 and len(C) == 1:
        answer.extend(max(A, B, C))'''
    print mid_a, mid_b, mid_c
    i = min(A[mid_a], B[mid_b], C[mid_c])
    j = max(A[mid_a], B[mid_b], C[mid_c])
    print i, j
    #a= math.log(na,2)
    #while a > 0:
    #while len(answer) <= a:
    # i is minimum and j is maximum in the medians
    while len(answer) < length:
        if i == A[mid_a] and j == B[mid_b]:
            if na >= nb:
                answer.extend(B[mid_b:])
                #a = a + len(B[mid_b:])
                rec_A = A[mid_b:]
                rec_B = B[:mid_b]
                rec_C = C
                print rec_A, rec_B, rec_C
                hunters(rec_A,rec_B,rec_C, length)
            else:
                answer.extend(B[-mid_a:])
                #a = a + len(B[mid_b:])
                rec_A = A[mid_a:]
                rec_B = B[:-mid_a]
                rec_C = C
                print rec_A, rec_B, rec_C
                hunters(rec_A,rec_B,rec_C, length)
        elif i == A[mid_a] and j == C[mid_c]:
            if na >= nc:
                answer.extend(C[mid_c:])
                #a = a + len(B[mid_b:])
                rec_A = A[mid_c:]
                rec_B = B
                rec_C = C[:mid_c]
                print rec_A, rec_B, rec_C
                hunters(rec_A,rec_B, rec_C, length)
            else:
                answer.extend(C[-mid_a:])
                #a = a + len(B[mid_b:])
                rec_A = A[mid_a:]
                rec_B = B
                rec_C = C[:-mid_a]
                print rec_A, rec_B, rec_C
                hunters(rec_A,rec_B, rec_C, length)
        elif i == B[mid_b] and j == A[mid_a]:
            if na >= nb:
                answer.extend(A[-mid_b:])
                #a = a + len(B[mid_a:])
                rec_A = A[:-mid_b]
                rec_B = B[mid_b:]
                rec_C = C
                print rec_A, rec_B, rec_C
                hunters(rec_A, rec_B, rec_C, length)
            else:
                answer.extend(A[mid_a:])
                #a = a + len(B[mid_a:])
                rec_A = A[:mid_a]
                rec_B = B[mid_a:]
                rec_C = C
                print rec_A, rec_B, rec_C
                hunters(rec_A, rec_B, rec_C, length)
        elif i == B[mid_b] and j == C[mid_c]:
            if nb >= nc:
                answer.extend(C[mid_c:])
                #a = a + len(B[mid_a:])
                rec_A = A
                rec_B = B[mid_c:]
                rec_C = C[:mid_c]
                print rec_A, rec_B, rec_C
                hunters(rec_A, rec_B, rec_C, length)
            else:
                answer.extend(C[-mid_b:])
                #a = a + len(B[mid_a:])
                rec_A = A
                rec_B = B[mid_b:]
                rec_C = C[:-mid_b]
                print rec_A, rec_B, rec_C
                hunters(rec_A, rec_B, rec_C, length)
        elif i == C[mid_c] and j == A[mid_a]:
            if nc >= na:
                answer.extend(A[mid_a:])
                rec_A = A[:mid_a]
                rec_B = B
                rec_C = C[mid_a:]
                print rec_A, rec_B, rec_C
                hunters(rec_A, rec_B, rec_C, length)
            else:
                answer.extend(A[-mid_c:])
                rec_A = A[:-mid_c]
                rec_B = B
                rec_C = C[mid_c:]
                print rec_A, rec_B, rec_C
                hunters(rec_A, rec_B, rec_C, length)
        elif i == C[mid_c] and j == B[mid_b]:
            if nc >= nb:
                answer.extend(B[mid_b:])
                rec_A = A
                rec_B = B[:mid_b]
                rec_C = C[mid_b:]
                print rec_A, rec_B, rec_C
                hunters(rec_A, rec_B, rec_C, length)
            else:
                answer.extend(B[-mid_c:])
                rec_A = A
                rec_B = B[:-mid_c]
                rec_C = C[mid_c:]
                print rec_A, rec_B, rec_C
                hunters(rec_A, rec_B, rec_C, length)
            #a = a-1
    return answer

if __name__ == '__main__':
    A = [239,246,290,390,512,629,689,833,906,952]
    B = [14,44,65,183,303,689,792,869,872,985]
    C = [157,187,285,312,323,358,456,634,718,891]
    length = (len(A)+len(B)+len(C))/2
    print "Half length is", length
    print "A:", A
    print "B:", B
    print "C:", C
    print "Sorted array after merge sort", hunters(A,B,C,length)