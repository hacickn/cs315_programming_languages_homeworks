#include <stdio.h>
int main() {
// 1. Iteration statements provided
// Iterations are provided in c by using while, for and do while loops
printf("1. Iteration statements provided \n");
int number = 0;
int trace = 0;
printf("while loop -----\n");
while( trace < 5 ){
    printf("Value of trace : %d in while loop\n", trace);
    trace++;
}
printf("Trace is reached to 5 \n\n");

printf("for loop -----\n");
for(int i = 0; i < 5; i++){
    printf("Value of i : %d in for loop\n", i);
}
printf("i is reached to 5 \n\n");

printf("do while loop -----\n");
do{ 
    printf("Value of number : %d in do-while loop\n", number);
    number++;
}while(number < 5);
printf("number is reached to 5 \n\n\n");
// 2. Data structures suitable for iteration
// Built in data structures are in c array
printf("2. Data structures suitable for iteration \n");
char array1[] = {'h','a','c','i'};
int array2[] = {2,3,5,1,6,3};
for(int i = 0; i < 4; i++){
    printf("%d. letter of haci is %c \n", i+1,array1[i]);
}

printf("\n");
trace = 0;
while(array2[trace] != 6){
    printf("6 is not found until %d. element \n",trace);
    trace++;
}


// 3. The way the next item is accessed
printf("3. The way the next item is accessed");
int num1 = 0;
printf("while---");
while ( num1 < 11 ){
    if( num1 == 6 ){
        printf("num1 Reached to 6\n");
        num1 += 2;
    }
    num1 = num1 + 1;
    printf("Turn %d times", num1);
    printf("\n");
}
printf("\nfor---");
for(int a = 0; a < 10; a = a+2){
    printf("Current value is %d \n",a );
}

    return 0;
}