#!/usr/bin/env python3
"""
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such
as IV and XL.

For the input XIV, for instance, you should return 14.
"""

VALUES = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def compare_characters(a: str, b: str) -> int:
    if a == b:
        return 0
    if a == "M" or b == "I":
        return -1
    if b == "M" or a == "I":
        return 1
    if a == "D" or b == "V":
        return -1
    if b == "D" or a == "V":
        return 1
    if a == "C" or b == "X":
        return -1
    if b == "C" or a == "X":
        return 1


def compute_word(w: str) -> int:
    total = 0
    intermediate = VALUES[w[0]]
    for i in range(1, len(w)):
        compare_result = compare_characters(w[i - 1], w[i])
        if compare_result == 0:
            intermediate += VALUES[w[i]]
            continue
        elif compare_result == 1:
            total -= intermediate
        else:
            total += intermediate
        intermediate = VALUES[w[i]]
    total += intermediate
    return total

if __name__ == "__main__":
    assert compute_word("XIV") == 14
    assert compute_word("MCMXII") == 1912
    assert compute_word("MMXX") == 2020
    assert compute_word("MM") == 2000
    assert compute_word("IIV") == 3
    print("PASSED")