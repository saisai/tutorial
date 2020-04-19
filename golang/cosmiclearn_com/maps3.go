package main

import "fmt"

func main() {

    var countryCapitals map[string]string = map[string]string {
        "India": "New Delhi",
        "U.S.A": "Washinton DC",
        "Japan": "Tokyo"}

        delete(countryCapitals, "Japan")
        fmt.Println(countryCapitals)
}
