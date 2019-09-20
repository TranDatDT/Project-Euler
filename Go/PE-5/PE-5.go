package main

import (
	"fmt"
)

func gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}

	return a
}

func main() {
	n := 20

	lcm := 1

	for i := 2; i <= n; i++ {
		lcm = (lcm * i) / gcd(lcm, i)
	}

	fmt.Println(lcm)
}
