package main

import "fmt"

func main() {

	personSalray := make(map[string]int)
	personSalray["steve"] = 12000
	personSalray["jame"] = 1203300
	personSalray["john"] = 123000
	personSalray["onn"] = 112000
	fmt.Println("personSalary map contents :", personSalray)
}
