package main

import "fmt"

func main() {

    matrix := [][]int{

        []int{1,2,3},
        []int{3,4,5},
        []int{7,8,9},
    }
    for i := 0; i < len(matrix); i++ {
        fmt.Println(matrix[i])
    }
}
