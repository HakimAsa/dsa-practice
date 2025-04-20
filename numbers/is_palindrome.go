// solution for an integer to be palindromic in Go
package main

import "fmt"

//take an int param and return a bool
func is_palindrome(x int) bool{
 	if x < 0 || (x % 10 == 0 && x != 0) {
		return false
	}
 	rev := 0
 	temp := x
 	for temp > 0 {
		digit := temp % 10
		rev = rev * 10 + digit
		temp /= 10
 	}
	return rev == x
}

func main  () {
	x := 121
	fmt.Println(is_palindrome(x))//true
	fmt.Println(is_palindrome(-x)) //false
	fmt.Println(is_palindrome(10)) //false
}