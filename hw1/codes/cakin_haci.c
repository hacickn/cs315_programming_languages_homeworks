#include<stdio.h>

int myfunction1() {
       
        printf(" * 1st function * ");
        return 0;
      }
int myfunction2() {
         printf(" * 2st function * ");
        return 1;
      }
int myfunction3() {
         printf(" * 3st function * ");
        return 0;
      }

int main()
{   

    /*
    1. Boolean Operators Provided
    &&	and
	||	or
	!	not
    */
    printf("1. Boolean Operators Provided \n\n");


    /*
    2. Data types for operands of boolean operators
    int
    */
    printf("2. Data types for operands of boolean operators \n\n");
    int num1 = 0;
    int num2 = 1;
    int num3 = 2;
    printf("bool value of 0 =  %d \n" , !!num1);
    printf("bool value of 1 =  %d \n" , !!num2);
    printf("bool value of 2 =  %d \n" , !!num3);
    printf("0 and 1 =  %d \n" , num1 && num2);
    printf("0 or 1 =  %d \n" ,  num1 || num2);
    printf("not 0 and 1 =  %d \n" ,  !num1 && num2);
    printf("\n\n");

    /*
    3. Operator precedence rules in descending order
    1 --> ()     
    2 --> not     
    3 --> and 
    4 --> or  
    */
    printf("3. Operator precedence rules in descending order \n\n");
    printf("True and True or False = %d \n", num2 && num2 || num1);
    printf("True or True and False = %d \n", num2 ||  num2 && num1);
    printf("False or True and False = %d \n", num1 ||  num2 && num1);
    printf("False or True and False = %d \n", num1 ||  num2 && num1);
    printf("True and True and (True or True) and False = %d \n", num2 && num2 && (num2 || num2) && num1);
    printf("True and True and not (True or True) and False = %d \n", num2 && num2 && !(num2 ||  num2) && num1);
    printf("True and True and True or True and False = %d \n", num2 && num2 && num2 ||  num2 && num1);
    printf("True and not True and True or True and False = %d \n", num2 && ! num2 && num2 ||  num2 && num1);
    printf("\n\n");


    /*
    4. Operator associativity rules for bool operators
    1 --> and, or, == , != ---> left associativity.
    */
    printf("4. Operator associativity rules for bool operator \n\n");
    printf("True and True and False => %d \n", num2 && num2 && num1);
    printf("True or True or False => %d \n",    num2 || num2 || num1);
    printf("True == True == False => %d \n",  num2 == num2 == num1);
    printf("True != True != False => %d \n",    num2 != num2 != num1);
    printf("\n\n");

    /*
    5. Operand evaluation order
    LEFT -> RIGHT in c
    */
    printf("5. Operand evaluation order \n\n");
    printf("myfunction1() and myfunction2() and myfunction3() = %d \n", myfunction1() && myfunction2() && myfunction3());
    printf("myfunction1() or myfunction2() or myfunction3() = %d \n", myfunction1() || myfunction2() || myfunction3());
    printf("myfunction1() == myfunction2() == myfunction3() = %d \n", (myfunction1() == myfunction2()) == myfunction3());
    printf("myfunction1() != myfunction2() != myfunction3() = %d \n", (myfunction1() != myfunction2()) != myfunction3());
    printf("\n\n");


    /*
    6. short-circuit evoluation
    LEFT -> RIGHT in c
    */
    printf("6. short-circuit evoluation \n\n");
    printf("These exapmles shows that c has short circuit \n");
    printf("myfunction1() and myfunction2() and myfunction3() = %d \n", myfunction1() && myfunction2() && myfunction3());
    printf("myfunction1() or myfunction2() or myfunction3() = %d \n", myfunction1() || myfunction2() || myfunction3());
    printf("myfunction1() == myfunction2() == myfunction3() = %d \n", (myfunction1() == myfunction2()) == myfunction3());
    printf("myfunction1() != myfunction2() != myfunction3() = %d \n", (myfunction1() != myfunction2()) != myfunction3());
    printf("\n\n");
    return 0;
}