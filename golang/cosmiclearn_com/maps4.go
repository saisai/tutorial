package main

import "fmt"

func main() {

    var countryCapitals map[string]string = map[string]string {

        "India": "New Delhi",
        "U.S.A": "Washinton DC",
        "Japan": "Tokyo",
    }

    value, exists := countryCapitals["France"]
    fmt.Println("Does France exist in out capital map ",value,  exists)


    value2, exists2 := countryCapitals["Japan"]
    fmt.Println("Does Japan exist in our capital map ", exists2)
    fmt.Println("Value = ", value2)
    
    
}
