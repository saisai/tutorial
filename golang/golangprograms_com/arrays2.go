package main

import "fmt"

func main() {
	var theArray [3]string

	theArray[0] = "India"   // assign a value to the first  element
	theArray[1] = "Candana" // assign a value tothe second element
	theArray[2] = "Japan"   // assign a vlue to the third element

	fmt.Println(theArray[0]) // access teh first element value
	fmt.Println(theArray[1]) // access teh second element value
	fmt.Println(theArray[2]) // access teh third element value
}
