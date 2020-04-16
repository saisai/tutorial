package main

import (
    "fmt"
    "container/ring"
)

func main() {
    // create a new ring of size 5
    r := ring.New(5)

    // get the length of the ring
    n := r.Len()

    // initialzie the ring with some integer values
    for i := 0; i < n; i++ {
        r.Value = i
        r = r.Next()
    }

    // Iterate thourhg the ring and print its contents
    r.Do(func(p interface{}){
        fmt.Println(p.(int))
    })
}
