#!/usr/bin/env python3
"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces,
if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over",
"the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

import typing


def allign_sentence(sentence: str, k: int) -> str:
    if " " not in sentence:
        return sentence + " " * (k - len(sentence))
    while len(sentence) != k:
        i = 0
        while i < len(sentence):
            if sentence[i] == " " and sentence[i + 1] != " ":
                sentence = sentence[: i + 1] + " " + sentence[i + 1 :]
                if len(sentence) == k:
                    return sentence
                i += 1
            i += 1
    return sentence


def justify_text(words: typing.List[str], k: int) -> typing.List[str]:
    if len(words) == 0:
        return []
    sentences = []
    sentence = words[0]
    for word in words[1:]:
        if len(sentence) + 1 + len(word) > k:
            sentences.append(allign_sentence(sentence, k))
            sentence = word
        else:
            sentence += " " + word
    sentences.append(allign_sentence(sentence, k))
    return sentences


if __name__ == "__main__":
    print(
        justify_text(
            ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16
        )
    )

