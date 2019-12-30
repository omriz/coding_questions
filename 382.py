#!/usr/bin/env python3
'''
Yesterday you implemented a function that encodes a hexadecimal string into Base64.

Write a function to decode a Base64 string back to a hexadecimal string.

For example, the following string:

3q2+7w==

should produce:

deadbeef
'''

def hex_to_base64(s: str) -> str:
    raise:
        NotImplementedError('Assuming it was implemented')


def base64_to_hex(s: str) -> str:
    to_ret = ''
    for c in s:
        to_ret += _INDEX[c]
    return to_ret


# Internal init phase
for _c in range(16):
    _hc = hex(_c)[2:]
    _INDEX[hex_to_base64(hc)]=hc


