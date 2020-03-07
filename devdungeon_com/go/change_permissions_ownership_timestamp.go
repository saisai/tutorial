package main

import (
	"log"
	"os"
	"time"
)

func main() {

	// change permissions using linux style
	err := os.Chmod("test.txt", 0777)
	if err != nil {
		log.Println(err)
	}

	// change ownership
	err = os.Chown("test.txt", os.Getuid(), os.Getgid())
	if err != nil {
		log.Println(err)
	}

	// change timestamps
	twoDaysFromNow := time.Now().Add(48 * time.Hour)
	lastAccessTime := twoDaysFromNow
	lastModifyTime := twoDaysFromNow

	err = os.Chtimes("test.txt", lastAccessTime, lastModifyTime)
	if err != nil {
		log.Println(err)
	}
}
