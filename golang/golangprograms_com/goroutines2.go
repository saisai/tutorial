package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
	"io/ioutil"
)

// watigroup is used to wait for the program to finish goroutines.
var wg sync.WaitGroup

func responseSize(url string) {
	// schedule the call to waitgroup's done to tell goroutine is complteded.

	defer wg.Done()

	fmt.Println("Step1 :", url)
	response, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Step2 :", url)
	defer response.Body.Close()

	fmt.Println("Step3 :", url)
	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Step4 :", len(body))
}

func main() {
	// add a count of there, one for each goroutine
	wg.Add(3)

	fmt.Println("Start Goroutines")

	go responseSize("https://www.golangprograms.com")
	go responseSize("https://stackoverflow.com")
	go responseSize("https://coderwall.com")

	// Wait for the goroutines to finish.

	wg.Wait()
	fmt.Println("Terminating Program")

}
