#!/usr/bin/env python3

import typing


def find_max_range_in_array(
    arr: typing.List[int],
) -> typing.Optional[typing.Tuple[int, int]]:
    if not arr:
        return None
    sorted_arr = sorted(arr)
    min_range = sorted_arr[0]
    max_range = sorted_arr[0]
    current_min = sorted_arr[0]
    current_max = sorted_arr[0]
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == current_max + 1:
            current_max = sorted_arr[i]
            if current_max - current_min > max_range - min_range:
                max_range = current_max
                min_range = current_min
        else:
            current_max = sorted_arr[i]
            current_min = sorted_arr[i]
    return min_range, max_range


if __name__ == "__main__":
    print(find_max_range_in_array([9, 6, 1, 3, 8, 10, 12, 11]))
