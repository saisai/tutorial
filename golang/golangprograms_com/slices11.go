package main

import "fmt"

func main() {
	var strSlice = []string{"India", "Canada", "Japan", "Germany", "Italy"}

	fmt.Println("\n------------- Example 1 -----------------\n")
	for index, element := range strSlice {
		fmt.Println(index, "--", element)
	}

	fmt.Println("\n---------------Example 2 --------------------\n")
	for _, value := range strSlice {
		fmt.Println(value)
	}

	fmt.Println("\n---------------Example 3 --------------------\n")
	j := 0
	for range strSlice {
		fmt.Println(strSlice[j])
		j++
	}
	
	fmt.Println("\n---------------Example 4 --------------------\n")
	for i := 0; i <len(strSlice); i++ {
		fmt.Println(strSlice[i])
	}
}
