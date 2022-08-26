package main

import "fmt"

/*
Given a collection of intervals,
find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8),
return 1 as the last interval can be removed and the first two won't overlap.
*/

type Interval struct {
	Start int
	End   int
}

// WhoToRemove finds which element has the most touches and asks to remove it.
func WhoToRemove(intervals []Interval) int {
	parallels := map[int]int{}
	for i := 0; i < len(intervals); i++ {
		for j := i + 1; j < len(intervals); j++ {
			f := false
			if intervals[i].Start < intervals[j].Start && intervals[i].End > intervals[j].Start {
				f = true
			}
			if intervals[i].End > intervals[j].End && intervals[i].Start < intervals[j].End {
				f = true
			}
			if intervals[i].Start < intervals[j].Start && intervals[i].End > intervals[j].End {
				f = true
			}
			if intervals[i].Start > intervals[j].Start && intervals[i].End < intervals[j].End {
				f = true
			}
			if f {
				if _, found := parallels[i]; found {
					parallels[i] += 1
				} else {
					parallels[i] = 1
				}
				if _, found := parallels[j]; found {
					parallels[j] += 1
				} else {
					parallels[j] = 1
				}
			}
		}
	}
	if len(parallels) == 0 {
		return -1
	}
	m := -1
	i := -1
	for k, v := range parallels {
		if v > m {
			m = v
			i = k
		}
	}
	return i
}

// NumToRemove returns the amount of intervals that needs to be removed.
func NumToRemove(intervals []Interval) int {
	i := WhoToRemove(intervals)
	if i == -1 {
		return 0
	}
	return 1 + NumToRemove(append(intervals[:i], intervals[i+1:]...))
}

func main() {
	fmt.Printf("Remove %d\n", NumToRemove([]Interval{
		{7, 9}, {2, 4}, {5, 8},
	}))
}
