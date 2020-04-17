package main

import "fmt"

func main() {

    var i int = 10
    i++
    fmt.Printf("i++ = %d\n", i)


    var ii int = 10
    ii--
    fmt.Printf("ii-- = %d\n", ii)

    var a int = 10
    fmt.Printf("+a = %d\n", +a)
    fmt.Printf("-a = %d\n", -a)

    var b int = 2
    fmt.Printf("^i = %d\n", ^b)

    var c bool = true
    fmt.Printf("!c = %t\n", c)

    var d int = 4
    var e int = 2
    fmt.Printf("d ^ e = %d\n", d ^ e)


    // shift operators
    var f uint = 4
    var g uint = 2

    fmt.Printf("f << g = %d\n", f << g)
    fmt.Printf("f >> g = %d\n", f >> g)


    var h int = 4
    var j int = 2
    fmt.Printf("h & j = %d\n", h & j)
    fmt.Printf("h | j = %d\n", h | j)
    fmt.Printf("h ^ j = %d\n", h ^ j)


    var isPlanet bool = false
    var isComet bool = false
    var isMeteor bool = false

    if(!isPlanet && !isComet) {
        isMeteor = true
        fmt.Printf("isPlanet = %t\n", isPlanet)
        fmt.Printf("isComet = %t\n", isComet)
        fmt.Printf("isMeteor = %t\n", isMeteor)

    }

    var isP bool = false
    var isM bool = true
    var isC bool = true

    if(isP || isC) {
        isM = false
        fmt.Printf("isP = %t\n", isP)
        fmt.Printf("isC = %t\n", isC)
        fmt.Printf("isM = %t\n", isM)
    }
}

