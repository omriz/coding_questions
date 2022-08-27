package main

import (
	"fmt"
	"os"
)

/*
You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'.
Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.
*/

// Optional solution:
// Count the letters ( in a map)
// For every go for every number-word (zero..nine) and check if they can be assembled (can be done multiple times for each word)
// Print it out

var wordToNum = map[string]int{
	"zero":  0,
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

func Contains(num string, letters map[rune]int) int {
	con := true
	for _, c := range num {
		if _, ok := letters[c]; !ok || letters[c] == 0 {
			con = false
		}
	}
	if !con {
		return -1
	}
	for _, c := range num {
		letters[c] -= 1
	}
	return wordToNum[num]
}

func Reconstruct(word string) []int {
	toReturn := []int{}
	letters := map[rune]int{}
	for _, c := range word {
		if _, ok := letters[c]; ok {
			letters[c] += 1
		} else {
			letters[c] = 1
		}
	}
	for _, num := range []string{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"} {
		a := Contains(num, letters)
		for a != -1 {
			toReturn = append(toReturn, a)
			a = Contains(num, letters)
		}
	}
	return toReturn
}

func main() {
	fmt.Printf("%v\n", Reconstruct(os.Args[1]))
}
