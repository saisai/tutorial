package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"sync"
	)
	
// WaitGroup is used to wait for the program to finish goroutines.

var wg sync.WaitGroup

func responseSize(url string, nums chan int) {
	// Schedule the call to WaitGroup's Done to tell goroutine is completed.
	
	defer wg.Done()
	
	response, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	
	defer response.Body.Close()
	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Fatal(err)
	}
	
	// send value to the unbeffered channel
	nums <- len(body)
}

func main() {
	nums := make(chan int) // declare a unbuffered channel 
	wg.Add(1)
	go responseSize("https://www.golangprograms.com", nums)
	fmt.Println(<-nums) // Read the value from unbuffered channel
	wg.Wait()
	close(nums) // Closes the channel
}