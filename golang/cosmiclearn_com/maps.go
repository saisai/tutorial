package main

import "fmt"

func main() {

    var countryCapitals map[string]string
    countryCapitals = make(map[string]string)
    countryCapitals["India"] = "New Delhi"
    countryCapitals["U.S.A"] = "Washington DC"
    countryCapitals["Japan"] = "Tokyo"

    fmt.Println(countryCapitals)
    fmt.Println(countryCapitals["India"])
}
