package main

import "fmt"

/*
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
*/

type Node struct {
	Next  *Node
	Value int
}

func SwapList(start *Node) *Node {
	n := start
	if n == nil || n.Next == nil {
		return n
	}
	a := n.Next
	toBe := a.Next
	a.Next = n
	n.Next = SwapList(toBe)
	return a
}

func main() {
	l := &Node{
		&Node{
			&Node{
				&Node{
					nil,
					4,
				},
				3,
			},
			2,
		},
		1,
	}
	l = SwapList(l)
	for l != nil {
		fmt.Printf("%d->", l.Value)
		l = l.Next
	}
}
