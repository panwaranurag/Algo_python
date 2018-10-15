import math
import sys

def isprime(n):
    if n <= 1 or n ==2 or n%2 == 0:
        return False
    m = int(math.sqrt(n))
    
    for i in range(3,m+1,2):
        if n%i == 0:
            return False 
    return True

if __name__ == '__main__' and len(sys.argv)!= 2:
    print "Enter the value of the number to be check"

if __name__ == '__main__' and len(sys.argv) == 2:
    number = int(sys.argv[1])
    print isprime(number)
    