package main


import "fmt"

func main() {

    i, j := 42, 2731

    p := &i     // point to i
    fmt.Println(*p) // read i through the pointer
    fmt.Println(&p)
    fmt.Println(&i)
    *p = 21 // set i through the pointer
    fmt.Println(&*p)
    fmt.Println(i) // see the new value of i

    p = &j // point to j
    *p = *p / 37 // divide j thourgh the pointer
    fmt.Println(j) // see the new value of j
}
