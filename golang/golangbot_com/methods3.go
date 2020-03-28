package main

import (
    "fmt"
)

type Employee struct {
    name    string
    age     int
}

// method with value reciever
func (e Employee) changeName(newName string) {
    e.name = newName
}

// method with pointer receiver
func (e *Employee) changeAge(newAge int) {
    e.age  = newAge
}

func main() {
    e := Employee {
        name: "Mark Andrew",
        age:    50,
    }

    fmt.Printf("Employee name vefore change: %s", e.name)
    e.changeName("Michael Andres")
    fmt.Printf("\nEmployee name after chage: %s", e.name)

    fmt.Printf("\n\nEmployee age before change: %d", e.age)
    (&e).changeAge(51)
    fmt.Printf("\nEmployee age after change: %d", e.age)
}
