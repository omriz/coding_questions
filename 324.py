import typing

def mice_to_holes(mice: typing.List[int], holes: typing.List[int]) -> int:
    if len(mice) != len(holes):
        raise ValueError('Number of mice must equal number of holes')
    if len(mice) == 0:
        return 0
    # 2 * nlog(n)
    mice.sort()
    holes.sort()
    diff = 0
    # n
    for i in range(len(mice)):
        if abs(mice[i] - holes[i]) > diff:
            diff = abs(mice[i] - holes[i])
    return diff

if __name__ == '__main__':
    print(mice_to_holes([1, 4, 9, 15], [10, -5, 0, 16]))
