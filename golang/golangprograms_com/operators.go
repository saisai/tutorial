/*
Comparison Operators

Comparison operators are used to compare two values.
Operator 		Name 						Example 	Result
== 				Equal 						x == y 		True if x is equal to y
!= 				Not equal 					x != y 		True if x is not equal to y
< 				Less than 					x < y 		True if x is less than y
<= 				Less than or equal to 		x <= y 		True if x is less than or equal to y
> 				Greater than 				x > y 		True if x is greater than y
>= 				Greater than or equal to 	x >= y 		True if x is greater than or equal to y
*/

package main

import "fmt"

func main() {

	var x, y = 15, 25

	fmt.Println(x == y)
	fmt.Println(x != y)
	fmt.Println(x < y)
	fmt.Println(x <= y)
	fmt.Println(x > y)
	fmt.Println(x >= y)

}
