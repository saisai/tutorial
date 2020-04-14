package main

import (

    "fmt"
    "os"
)

func main() {

    f, err := os.Open("/test.txt")

    if err, ok := err.(*os.PathErro); ok {
        fmt.Println("File at path ", err.Path, "Failed to open")
        return
    }
    fmt.Println(f.Name(), "opened sucessfully")
}
