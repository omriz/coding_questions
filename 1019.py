#!/usr/bin/env python3
'''
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
'''

class Rect(object):
    def __init__(self,tl, tr, bl, br):
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br


# I can probably do this without all the helper structs - but it makes it easier to understand for my test.
# From a performance POV - it doesn't matter that much, it's still O(1) in both Memory and time
def calc_interssect(rect1, rect2):
    r1 = Rect(
        rect1["top_left"],
        (rect1["top_left"][0]+rect1["dimensions"][0], rect1["top_left"][1]),
        (rect1["top_left"][0], rect1["top_left"][1]-rect1["dimensions"][1]),
        (rect1["top_left"][0]+rect1["dimensions"][0], rect1["top_left"][1]-rect1["dimensions"][1]))
    r2 = Rect(
        rect2["top_left"],
        (rect2["top_left"][0]+rect2["dimensions"][0], rect2["top_left"][1]),
        (rect2["top_left"][0], rect2["top_left"][1]-rect2["dimensions"][1]),
        (rect2["top_left"][0]+rect2["dimensions"][0], rect2["top_left"][1]-rect2["dimensions"][1]))
    if r1.bl[1] >= r2.tl[1] or r2.bl[1] >= r1.tl[1]:
        return 0
    if r1.tr[0] <= r2.tl[0] or r2.tr[0] <= r1.tl[0]:
        return 0
    intersect = Rect(
        (max(r1.tl[0],r2.tl[0]),min(r1.tl[1],r2.tl[1])),
        (min(r1.tr[0],r2.tr[0]),min(r1.tr[1],r2.tr[1])),
        (max(r1.bl[0],r2.bl[0]),max(r1.bl[1],r2.bl[1])),
        (min(r1.br[0],r2.br[0]),max(r1.br[1],r2.br[1])),
    )
    return (intersect.tr[0] - intersect.tl[0])*(intersect.tl[1] - intersect.bl[1])

def main():
    rect1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    }
    rect2 = {
        "top_left": (0, 5),
        "dimensions": (4, 3) # width, height
    }
    print(calc_interssect(rect1, rect2))

if __name__ == '__main__':
    main()