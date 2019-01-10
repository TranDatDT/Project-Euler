/*
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers
*/

package main

import (
	"fmt"
	"strconv"
)

func Reverse(s string) string {
	// Reverse a string
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func main() {
	max_number := -1;
	for num1 := 999; num1 > -1; num1-- {
		for num2 := 999; num2 > -1; num2 -- {
			mul := num1 * num2;
			str_mul := strconv.Itoa(mul)
			if str_mul == Reverse(str_mul) {
				if mul > max_number {
					max_number = mul;
				}
			}
		}
	}
	fmt.Println(max_number);
}