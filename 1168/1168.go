package main

import "fmt"

/*
The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order.
By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, determine whether
it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.
*/

func IsPossible(arr []int, target int) bool {
	// No number to check - we're out.
	if len(arr) == 0 {
		return false
	}
	// We reached the result !
	if len(arr) == 1 && arr[0] == target {
		return true
	}
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			newArr := []int{}
			for k := 0; k < len(arr); k++ {
				if !(k == j || k == i) {
					newArr = append(newArr, arr[k])
				}
			}
			elem := arr[i] + arr[j]
			if IsPossible(append(newArr, elem), target) {
				return true
			}
			elem = arr[i] - arr[j]
			if IsPossible(append(newArr, elem), target) {
				return true
			}
			elem = arr[j] - arr[i]
			if IsPossible(append(newArr, elem), target) {
				return true
			}
			elem = arr[i] * arr[j]
			if IsPossible(append(newArr, elem), target) {
				return true
			}
			if arr[j] != 0 && arr[i]%arr[j] == 0 {
				elem = arr[i] / arr[j]
				if IsPossible(append(newArr, elem), target) {
					return true
				}
			}
			if arr[i] != 0 && arr[j]%arr[i] == 0 {
				elem = arr[j] / arr[i]
				if IsPossible(append(newArr, elem), target) {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	fmt.Printf("IsPossible %t\n", IsPossible([]int{5, 2, 7, 8}, 24))
}
