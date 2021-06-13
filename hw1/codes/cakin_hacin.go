package main

import (
	"fmt"
)

func main() {
	var bool1 = false
	var bool2 = true


	/*
    1. Boolean Operators Provided
    &&	and
	||	or
	!	not
    */
    fmt.Println("1. Boolean Operators Provided ")


    /*
    2. Data types for operands of boolean operators
    bool
    */
    fmt.Println("2. Data types for operands of boolean operators ");

	fmt.Println("false and true = " , bool1 && bool2)
    fmt.Println("false or true = " ,  bool1 || bool2)
    fmt.Println("not false and true = " ,  !bool1 && bool2)

	/*
    3. Operator precedence rules in descending order
    1 --> ()     
    2 --> not     
    3 --> and 
    4 --> or  
    */

	fmt.Println("3. Operator precedence rules in descending order ");
    fmt.Println("False and True or not False = ", (bool1 && bool2 || !bool1));
    fmt.Println("False or True and not False = ", (bool1 ||  bool2 && !bool1));
    fmt.Println("False and True and not False = ", (bool1 &&  bool2 && !bool1));
    fmt.Println("False or True or not False = ", (bool1 ||  bool2 || !bool1));
    fmt.Println("True and not True and (True or not True) and False = ", (bool2 && !bool2 && (bool2 || !bool2) && bool1));
    fmt.Println("True and True and not (True or True) and False = ", (bool2 && bool2 && !(bool2 ||  bool2) && bool1));
    fmt.Println("True and not True and True or True and False = ", (bool2 && !bool2 && bool2 ||  bool2 && bool1));
    fmt.Println("True and not True and True or True and False = ", (bool2 && ! bool2 && bool2 ||  bool2 && bool1));
 

	/*
    4. Operator associativity rules for bool operators
    and,or left associativity, not right associvity.
    */
	fmt.Println("4. Operator associativity rules for bool operator ");
    fmt.Println("True and True and False => ", bool2 && bool2 && bool1);
    fmt.Println("True or True or False => ",    bool2 || bool2 || bool1);
    fmt.Println("True == True == False => ",  bool2 == bool2 == bool1);
    fmt.Println("True != True != False => ",    bool2 != bool2 != bool1);

    /*
    5. Operand evaluation order
    LEFT -> RIGHT in go
    */
    fmt.Println("5. Operand evaluation order \n\n");
    fmt.Println("myfunction1() and myfunction2() and myfunction3() = ", myfunction1() && myfunction2() && myfunction3());
    fmt.Println("myfunction1() or myfunction2() or myfunction3() = ", myfunction1() || myfunction2() || myfunction3());
    fmt.Println("myfunction1() != myfunction2() != myfunction3() = ", (myfunction1() != myfunction2()) != myfunction3());

	/*
    6. short-circuit evoluation
    LEFT -> RIGHT in c
    */
	fmt.Println("6. short-circuit evoluation \n\n");
    fmt.Println("myfunction1() and myfunction2() and myfunction3() = ", myfunction1() && myfunction2() && myfunction3());
    fmt.Println("myfunction1() or myfunction2() or myfunction3() = ", myfunction1() || myfunction2() || myfunction3());
    fmt.Println("myfunction1() != myfunction2() != myfunction3() = ", (myfunction1() != myfunction2()) != myfunction3());
}

func myfunction1() bool {
	fmt.Println(" * 1st function * ")
	return false 
 }

 func myfunction2() bool {
	fmt.Println(" * 2nd function * ")
	return true 
 }

 func myfunction3() bool {
	fmt.Println(" * 3rd function * ")
	return false 
 }