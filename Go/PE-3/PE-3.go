// https://projecteuler.net/problem=3

package main

import "fmt"

func max_prime(number int) int {
	var d int = 2
	for number > 1 {
		for number % d == 0 {
			number = number / d
		}
		d++
	}
	d--
	return d
}

func main() {
	fmt.Println(max_prime(600851475143))
}
