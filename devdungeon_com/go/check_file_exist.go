package main

import (
	"log"
	"os"
)

var (
	fileInfo *os.FileInfo
	err      error
)

func main() {
	// stat returns file info. it will return
	// an error if there is no file.
	fileInfo, err := os.Stat("test.txt")
	if err != nil {
		if os.IsNotExist(err) {
			log.Fatal("File doex not exist.")
		}
	}

	log.Println("File does exist. File information")
	log.Println(fileInfo)
}
