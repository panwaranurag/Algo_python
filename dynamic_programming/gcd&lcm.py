import sys

def GCD(a,b):
    if b == 0:
        return a
    return GCD(b,a%b)

def LCM(a,b):
    return (b*a)/GCD(a,b)

if __name__=='__main__' and len(sys.argv) != 3:
    print "Enter the value of a and b"
    
if __name__=='__main__' and len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print GCD(a,b)
    print LCM(a,b)