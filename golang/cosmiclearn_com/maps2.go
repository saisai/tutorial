package main

import "fmt"

func main() {

    var countryCapitals map[string]string = map[string]string{

        "India" : "New Delhi",
        "U.S.A" : "Washington DC",
        "Japan" : "Tokyo",
    }

    fmt.Println(countryCapitals)
    fmt.Println(countryCapitals["India"])
}
