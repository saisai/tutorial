package main

import (
	"fmt"
	"log"
	"os"
)

var (
	newFile *os.File
	err     error
)

func main() {
	fmt.Println("vim-go")

	newFile, err = os.Create("test.txt")

	if err != nil {
		log.Fatal(err)
	}

	log.Println(newFile)
	newFile.Close()

}
