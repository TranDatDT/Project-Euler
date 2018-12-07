package main

import "fmt"

func main() {
	fib1, fib2, sum := 0, 1, 0
	
	for fib1 < 4000000 {
		temp := fib1
		fib1 = fib2
		fib2 += temp
		if fib1 % 2 == 0 {
			sum += fib1
		}
	}

	fmt.Println(sum)
}
