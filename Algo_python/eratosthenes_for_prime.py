import sys

def eratosthenes2(n):
    multiples = set()
    for i in range(2,n+1):
        if i not in multiples:
            print (i)
            multiples.update(range(i*i,n+1, i))

if __name__ == '__main__' and len(sys.argv)!=2:
    print "Enter the number:"

if __name__ == '__main__' and len(sys.argv) == 2:
    number = int(sys.argv[1])
    print eratosthenes2(number)