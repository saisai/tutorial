package main

import (
	"bytes"
	"fmt"
	"os"
)

func main() {
	fmt.Println("vim-go")

	var b bytes.Buffer // a buffer needs to initialization
	b.Write([]byte("Hello "))
	fmt.Fprintf(&b, "world!")
	b.WriteTo(os.Stdout)
}
