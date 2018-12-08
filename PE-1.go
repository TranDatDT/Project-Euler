// https://projecteuler.net/problem=1

package main

import "fmt"

func main() {
	sum := 0

	for number := 0; number < 1000; number++ {
		if number % 3 == 0 || number % 5 == 0 {
			sum += number
		}
	}
	
	fmt.Println(sum)
}
