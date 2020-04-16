package main

import (
    "fmt"
    "container/ring"
)

func main() {
    // create two rings, r and s, of size 2
    r := ring.New(2)
    s := ring.New(2)

    // get the length of the ring
    lr := r.Len()
    ls := s.Len()

    // initialize r with 0s
    for i := 0; i < lr; i++ {
        r.Value = 0
        r = r.Next()
    }

     // initialzie s with 1s
     for j := 0; j < ls; j++ {
         s.Value = 1
         s = s.Next()
     }

     // link ring r and ring s
     rs := r.Link(s)

     // iterate through the combined ring and print its contents
     rs.Do(func(p interface{}){
         fmt.Println(p.(int))
     })
}
