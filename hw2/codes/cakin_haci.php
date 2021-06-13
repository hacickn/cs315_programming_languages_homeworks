<?php
// 1. Iteration statements provided
// Iterations are provided in php by using while, for, forEach and do while loops
$bool1 = true;
$num1 = 0;
printf("1. Iteration statements provided");
printf("while -----\n");
while($bool1){
    if($num1 == 5){
        printf("num1 reached to 5\n");
        break;
    }
    printf("num1 = %d \n", $num1);
    $num1++;
}
printf("do-while -----\n");
$num2 = 0;
do{
    $num2+=2;
    printf("num2 = %d \n", $num2);
} while( $num2 < 10 );

printf("for -----\n");
for($k = 0; $k < 6; $k++){
    if($k ==4){
        printf("Reached to 4\n");
        break;
    }
    printf("k = %d \n", $k);
}
printf("for-each -----\n");
$arrayNum = array(0, 1, 2);
foreach ($arrayNum as $value) {
   $value = $value + 4;
   printf("value = %d \n", $value);
   printf( "\n");
}


// 2. Data structures suitable for iteration
// Built in data structures is in php array
printf("2. Data structures suitable for iteration\n");
$arrayNum = array(0, 1, 2, 3, 4, 5);
foreach ($arrayNum as $value) {
    printf("value = %d \n", $value);
 }
printf( "\n");
 
$birthDay = array ("day"  => 24, "month" => 02, "year"   => 2000 );
 foreach ($birthDay as $name => $value) {
    printf("value = %d \n", $value);
 }

// 3. The way the next item is accessed
printf("3. The way the next item is accessed\n");
printf( "while-----\n");
$num3 = 0;
     while( $num3 < 10 ) {
     if ( $num3 == 4){
            printf("num3 reached 4\n");
           break;
         }
     printf("num3 = %d \n", $num3);
     $num3 = $num3 + 2;

     }
     // For Loop
     printf( "\nfor-----\n");
     for( $m= 0; $m< 10 ; $m++){
        if( $m == 4 ){
            printf("m reached 4\n");
            break;
        }
        printf("m = %d \n", $m);
        $m = $m + 1;
    }

?>
