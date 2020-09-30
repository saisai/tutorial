package employee

import "fmt"

type Employee struct {

    FirstName       string
    LastName        string
    TotalLeaves     int
    LeavesTaken     int
}

func (e Emplooyee) LeavesRemaining() {
    fmt.Printf("%s  %s has %d leaves remaining", e.FirstName, e.LastName, (e.TotalLeaves - e.LeavesTaken))
}
