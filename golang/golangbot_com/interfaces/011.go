
package main

import "fmt"

type Describer interface {
    Describe()
}

type Person struct {
    name string
    age  int
}

func (p Person) Describe() { // implemented using value receiver
    fmt.Printf("%s is %d years old\n", p.name, p.age)

}

type Address struct {

    state string
    country string
}

// implementd using pointer receiver
func (a *Address) Describe() {
    fmt.Printf("State %s Country %s", a.state, a.country)

}

func main() {

    var d1 Describer
    p1 := Person{"Sam", 25}
    d1 = p1
    d1.Describe()
    p2 := Person{"James", 32}
    d1 = &p2
    d1.Describe()

    var d2 Describer
    a := Address{"Washington", "USA"}

    /* Compilation error if the following line is
    uncommented
    cannot us a (type Address) as type Describer
    in assignmernt: Address does not implemtn
    Describer (Describe method ahs pointer receiver)
    */
    // d2 = a
    d2 = &a //this works since Describer interface 
    // is eimpletment by Address poitner ins line 22
    d2.Describe()
}
