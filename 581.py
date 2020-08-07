#!/usr/bin/env python3
"""
Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.

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
"""

import typing

class Rectangle(object):
    def __init__(self, top_left: typing.Tuple[int,int], dimensions: typing.Tuple[int,int]):
        self.top_left = top_left
        self.dimensions = dimensions


def get_corners(r1: rectangle) -> typing.Tuple[int,int, int]:
    r1_tl = r1.top_left
    r1_tr = (r1.top_left[0] + r1.dimensions[0], r1.top_left[1])
    r1_bl = (r1.top_left[0], r1.top_left[1] - r1.dimensions[1])
    r1_br = (r1.top_left[0] + r1.dimensions[0], r1.top_left[1] - r1.dimensions[1])
    return r1_tl, r1_tr, r1_bl

def intersection_area(r1: Rectangle, r2: Rectangle) -> typing.Optional[int]:
    r1_tl, r1_tr, r1_bl = get_corners(r1)
    r2_tl, r2_tr, r2_bl = get_corners(r2)
    int_tl = (0,0)
    if r1_tl[0] < r2_tl[0]:
        int_tl[0] = r2_tl[0]
        if r1_tl[1] < r2_tl[1]:
            int_tl[1] = r1_tl[1]
        else:
            int_tl[1] = r2_tl[1]
    else:
        int_tl[0] = r1_tl[0]
        if r2_tl[1] < r1_tl[1]:
            int_tl[1] = r2_tl[1]
        else:
            int_tl[1] = r1_tl[1]
    if r1_tr[0] > r2_tr[0]:
        int_tr_x = r2_tr[0]
    else:
        int_tr_x = r1_tr[0]
    if r1_bl[0] < r2_bl[0]:
        if r1_bl[1] < r2_bl[1]:
            int_bl_y = r2_bl[1]
        else:
            int_bl_y = r1_bl[1]
    else:
        if r2_bl[1] < r1_bl[1]:
            int_bl_y = r1_bl[1]
        else:
            int_bl_y = r2_bl[1]
    if int_tl[0] > int_tr_x:
        return None
    if int_bl_y > int_tl[1]:
        return None
    return (int_tr_x - int_tl[0]) * (int_tl[1] - int_bl_y)