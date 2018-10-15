import math
answer = []
rec_A = []
rec_B = []
rec_C = []
a = 0
def hunters(A,B,C, length):
    global answer, rec_A, rec_B,rec_C, a, b
    '''while not A or not B or not C:
        mergelist = A + B + C
        mergelist.sort()
        remaining = length - len(answer)
        answer.extend(mergelist[-remaining:])
        return answer 
        break'''
    '''if (not A and not B) and len(answer) < length:
        remain = length - len(answer)
        answer.extend(C[-remain:])
        return answer 
        break
    elif (not B and not C) and len(answer) < length:
        remain = length - len(answer)
        answer.extend(A[-remain:])
        return answer 
        break
    elif (not A and not C) and len(answer) < length:
        remain = length - len(answer)
        answer.extend(B[-remain:])
        return answer 
        break'''
    while not A or not B or not C:
        if (not A) and len(B) == 1:
            if B[1] >= C[len(C)//2]:
                remain = length - len(answer)
                answer.extend(B[1])
                answer.extend(C[-remain+1:])
                return answer 
                break
            else:
                remain = length - len(answer)
                answer.extend(C[-remain:])
                return answer 
                break
        elif (not A) and len(C) == 1:
            if C[1] >= B[len(B)//2]:
                remain = length - len(answer)
                answer.extend(C[1])
                answer.extend(B[-remain+1:])
                return answer 
                break
            else:
                remain = length - len(answer)
                answer.extend(B[-remain:])
                return answer 
                break
        elif (not B) and len(C) == 1:
            if C[1] >= A[len(A)//2]:
                remain = length - len(answer)
                answer.extend(C[1])
                answer.extend(A[-remain+1:])
                return answer 
                break
            else:
                remain = length - len(answer)
                answer.extend(A[-remain:])
                return answer 
                break
        elif (not B) and len(A) == 1:
            if A[1] >= A[len(C)//2]:
                remain = length - len(answer)
                answer.extend(A[1])
                answer.extend(C[-remain+1:])
                return answer 
                break
            else:
                remain = length - len(answer)
                answer.extend(C[-remain:])
                return answer 
                break
        elif (not C) and len(A) == 1:
            if A[1] >= B[len(B)//2]:
                remain = length - len(answer)
                answer.extend(A[1])
                answer.extend(B[-remain+1:])
                return answer 
                break
            else:
                remain = length - len(answer)
                answer.extend(B[-remain:])
                return answer 
                break
        elif (not C) and len(B) == 1:
            if B[1] >= A[len(A)//2]:
                remain = length - len(answer)
                answer.extend(B[1])
                answer.extend(A[-remain+1:])
                return answer 
                break
            else:
                remain = length - len(answer)
                answer.extend(A[-remain:])
                return answer 
                break
    na = len(A)
    nb = len(B)
    nc = len(C)
    mid_a = na//2
    mid_b = nb//2
    mid_c = nc//2
    print mid_a, mid_b, mid_c
    i = min(A[mid_a], B[mid_b], C[mid_c])
    j = max(A[mid_a], B[mid_b], C[mid_c])
    print i, j
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
    return "The upper half is", answer

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
    B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 30]
    C = [21, 22, 23, 24, 25, 26, 27, 28, 29, 40]
    length = (len(A)+len(B)+len(C))/2
    print "Half length is", length
    print "A:", A
    print "B:", B
    print "C:", C
    print "The recursion", hunters(A,B,C,length)