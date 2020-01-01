def calc_arr(arr, expected):
    if len(arr) == 2:
        return (
            arr[0] + arr[1] == expected or
            arr[0] - arr[1] == expected or
            float(arr[0]) / arr[1] == expected or
            arr[0] * arr[1] == expected
        )
    return (
        calc_arr(arr[1:], expected - arr[0]) or
        calc_arr(arr[1:], arr[0] - expected) or
        calc_arr(arr[1:], expected/float(arr[0])) or
        calc_arr(arr[1:], float(arr[0])/expected) or
        calc_arr([arr[0] + arr[1]] + arr[2:], expected) or
        calc_arr([arr[0] - arr[1]] + arr[2:], expected) or
        calc_arr([arr[0] * arr[1]] + arr[2:], expected) or
        calc_arr([float(arr[0]) / arr[1]] + arr[2:], expected)
    )

if __name__ == '__main__':
    print(calc_arr([5, 2, 7, 8], 24))