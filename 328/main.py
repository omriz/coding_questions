import math
import sys

def main():
    n = int(sys.argv[1])
    while n > 1 :
        s = int(math.floor(math.sqrt(n)))
        i = 2
        while i < s:
            if n % i == 0:
                n = int(n/i)
                print(n)
                break
            i+=1
        else:
            ss = s*s
            while n > ss and n > 1:
                print(n)
                n -= 1
            else:
                print(n)
            n = s

if __name__ == '__main__':
    main()
