package main

import "fmt"

/*
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
*/

const MAX_LOG_SIZE = 10

type Logger struct {
	lines []int
}

func (l *Logger) Record(order_id int) {
	l.lines = append([]int{order_id}, l.lines...)
	if len(l.lines) > MAX_LOG_SIZE {
		l.lines = l.lines[:len(l.lines)-1]
	}
}
func (l *Logger) GetLast(n int) int {
	return l.lines[n]
}

func main() {
	l := Logger{}
	l.Record(1)
	l.Record(2)
	l.Record(3)
	l.Record(4)
	l.Record(5)
	l.Record(6)
	l.Record(7)
	l.Record(8)
	l.Record(9)
	l.Record(10)
	l.Record(11)
	fmt.Printf("%d: %d", 4, l.GetLast(4))
}
