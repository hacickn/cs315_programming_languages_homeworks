

package main

import (
	"fmt"
)

func main() {
// 1. Iteration statements provided
// Iterations are provided in go by using while, for and forEach loops
fmt.Println("1. Iteration statements provided \n")
fmt.Println("while loop \n")
var bool1 = true
trace := 0
for bool1 {
	if trace == 5 {
		fmt.Println("Trace reached to 5 \n")
		break
	}
	fmt.Println("Current value in while loop is ", trace)
	trace = trace + 1
}


fmt.Println("\nfor loop \n")
for i :=0; i < 6; i++ {
	fmt.Println("Current value in for loop is ", i)
}

fmt.Println("\nforEach loop \n")
arrayEx := []int64{ 1907,2000,1883}
for place,value := range arrayEx {
	fmt.Println("Place : ", place , " Value : ", value)
}

// 2. Data structures suitable for iteration
// Built in data structures are in go array, slice
fmt.Println("\n2. Data structures suitable for iteration\n")
array1 := [4]int64{24,02,2000,1907}
fmt.Println("Array is ", array1)
for i := 0; i < 4; i++ {
	fmt.Println(i+1,". element is : ", array1[i])
}

fmt.Println("\n")
slice1 := [4]string{"KING","OF","THE","NOTRH"}
for place,value := range slice1 {
	fmt.Println("Place : ", place , " Value : ", value)
}

// 3. The way the next item is accessed
fmt.Println("\n3. The way the next item is accessed\n")
num2:= 0 
    for num2 < 8 {
        if  num2 == 6 {
            fmt.Println("Reached  '6'") 
            num2 = num2 + 2
			break
        }
        num2= num2 + 1
        fmt.Println(" Turn ", num2 , " times") 
    }
    fmt.Println("\n")


    for k := 0; k < 11; k = k +2 {
        if  k == 6 {
            fmt.Println("Reached  '6'") 
			break
        }
        fmt.Println(" Turn ", k , " times") 
    }

}
