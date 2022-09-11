package main

import (
	"flag"
	"fmt"
	"math"
)

/*
A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees.
For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
*/

func findStrob(digits int) []int {
	if digits == 0 {
		return []int{}
	}
	if digits == 1 {
		return []int{0, 1, 8}
	}
	if digits == 2 {
		return []int{11, 88, 69, 96}
	}
	numbers := []int{}
	for _, num := range findStrob(digits - 2) {
		numbers = append(numbers, int(math.Pow10((digits-1)))+num*10+1)
		numbers = append(numbers, 8*int(math.Pow10((digits-1)))+num*10+8)
		numbers = append(numbers, 6*int(math.Pow10((digits-1)))+num*10+9)
		numbers = append(numbers, 9*int(math.Pow10((digits-1)))+num*10+6)
	}
	return numbers
}

func main() {
	digits := flag.Int("digits", 0, "number of digits for the number.")
	flag.Parse()
	for _, a := range findStrob(*digits) {
		fmt.Printf("%d\n", a)
	}
}
