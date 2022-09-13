package main

import (
	"fmt"
	"math/rand"
)

/*
You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps.
Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
*/

type Probability struct {
	Source rune
	Dest   rune
	Prob   float32
}

func calcSteps(probs []Probability, steps int) map[rune]int {
	redirects := map[rune][]Probability{}
	for _, p := range probs {
		redirects[p.Source] = append(redirects[p.Source], p)
	}
	res := map[rune]int{}
	for k, _ := range redirects {
		res[k] = 0
	}
	location := 'a'
	for i := steps; i > 0; i-- {
		p := rand.Float32()
		prob := float32(0.0)
		for _, pp := range redirects[location] {
			if pp.Prob+prob > p {
				res[pp.Dest] += 1
				location = pp.Dest
				break
			}
			prob += pp.Prob
		}
	}
	return res
}

func main() {
	a := []Probability{
		{'a', 'a', 0.9},
		{'a', 'b', 0.075},
		{'a', 'c', 0.025},
		{'b', 'a', 0.15},
		{'b', 'b', 0.8},
		{'b', 'c', 0.05},
		{'c', 'a', 0.25},
		{'c', 'b', 0.25},
		{'c', 'c', 0.5},
	}
	fmt.Printf("Result %v", calcSteps(a, 5000))
}
