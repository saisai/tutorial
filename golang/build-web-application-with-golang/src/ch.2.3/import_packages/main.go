package main

import (
    // `_` will only call init() inside the package only_call_init
    _ "ch.2.3/import_packages/only_call_init"
    f "fmt"     // import the package as `f`
    . "math"    // makes the public methods and constants global
    "mymath"    // custom package located at $GOPATH/src/
    "os"        // normal import of a standard package
    "text/template" // the packge takes the name of last folder path, `template`
)

func main() {
    f.Println("mymath.Sqrt(4) =", mymath.Sqrt(4))
    f.Println("E = ", E) // reference math.E

    t, _ := template.New("test").Parse("Pi^2 = {{.}}")
    t.Execute(os.Stdout, Pow(Pi, 2))
}
