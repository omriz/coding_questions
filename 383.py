#!/usr/bin/env python3
import sys
import typing


def embolden(s: str, lst: typing.List[str]) -> str:
    ss = []
    for i in range(len(s)):
        for w in lst:
            if s[i : i + len(w)] == w:
                ss.append("<b>")
            if s[i - len(w) : i] == w:
                ss.append("</b>")
        ss.append(s[i])
    cc = 0
    aa = ""
    for a in ss:
        if a == "<b>":
            if cc > 0:
                cc += 1
            else:
                aa += "<b>"
                cc = 1
        elif a == "</b>":
            if cc == 1:
                aa += "</b>"
                cc = 0
            else:
                cc -= 1
        else:
            aa += a
    return aa


if __name__ == "__main__":
    print(embolden(sys.argv[1], sys.argv[2:]))
