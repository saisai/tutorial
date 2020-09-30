
package main

import "fmt"

type address struct {
    city    string
    state   string
}

func (a address) fullAddress() {
    fmt.Printf("full address: %s, %s", a.city, a.state)
}

type person struct {
    firstName string
    lastName string
    address
}

func main() {
    p := person {
        firstName: "Elon",
        lastName:   "MUsk",
        address:    address {
            city:   "Los Angeles",
            state:  "California",
        },
    }

    p.fullAddress() // aaccessing fullAddress method of address struct
}
