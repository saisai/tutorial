package main

import (
	"log"
	"os"
)

func main() {
	// Truncate a file to 100 bytes. If file
	// is less than 100 bytes the original contents will remain
	// at the beginning, and the rest of the space is
	// filled with null bytes. If it is over 100 bytes
	// Everything past 100 bytes will be lost. Either way
	// we will end up with exactly 100 bytes.
	// Pass in 0 to turncate to a completely empty file

	err := os.Truncate("text.txt", 100)
	if err != nil {
		log.Fatal(err)
	}
}
