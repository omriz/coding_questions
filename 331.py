#xyxxxyxyy
#101232321
import sys

def dual_flips(s):
    "Almost good"
    if len(s) <= 1:
        return 0
    x = 0
    y = len(s) -1
    flips = []
    while x<y:
        if s[x] == 'x':
            x += 1
            continue
        if s[y] == 'y':
            y -= 1
            continue
        flips.append(x)
        flips.append(y)
        x += 1
        y -= 1
    return sorted(flips)

def sums_flips(s):
    "Really good"
    if len(s) <= 1:
        return 0
    sums = [0]*len(s)
    if s[0] == 'x':
        sums[0] = 1
    else:
        sums[0] = -1
    for i in range(1,len(s)):
        if s[i] == 'x':
            sums[i] = sums[i-1] + 1
        else:
            sums[i] = sums[i-1] - 1
    m = sums[0]
    max_place = 0
    for i,v in enumerate(sums):
        if v > m:
            m = v
            max_place = i
    j=0
    flips = []
    if m > 0:
        while j <= max_place:
            if s[j] == 'y':
                flips.append(j)
            j += 1
        j=len(s)-1
        while j > max_place:
            if s[j] == 'x':
                flips.append(j)
            j -= 1
    if m < 0:
        while j < len(s):
            if s[j] == 'x':
                flips.append(j)
            j += 1
    return sorted(flips)

if __name__ == '__main__':
    print(dual_flips(sys.argv[1]))
    print(sums_flips(sys.argv[1]))
