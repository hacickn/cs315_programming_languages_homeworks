<?php
function myfunction1() {
    echo " * 1st function * ";
    return false;
  }

  function myfunction2() {
    echo " * 2nd function * ";
    return true;
  }

  function myfunction3() {
    echo " * 3rd function * ";
    return false;
  }
$bool1 = false;
$bool2 = true;
$bool3 = true;
/*
1. Boolean Operators Provided
&&	and
||	or
!	not
*/
echo("1. Boolean Operators Provided \n\n");

/*
2. Data types for operands of boolean operators
bool
*/
echo("2. Data types for operands of boolean operators \n\n");
echo "false and true = " , ($bool1 & $bool2), "\n";
echo "false or true =  " , ($bool1 or $bool2), "\n";
echo "not false and true = " ,  (!$bool1 and $bool2), "\n";
echo("\n\n");

/*
3. Operator precedence rules in descending order
1 --> ()     
2 --> not     
3 --> and 
4 --> or  
*/

echo("3. Operator precedence rules in descending order \n\n");
echo"True and True or False = ", ($bool2 & $bool2 | $bool1), "\n";
echo"True or True and False = ", $bool2 |  $bool2 & $bool1, "\n";
echo"False or True and False = ", $bool1 |  $bool2 & $bool1, "\n";
echo"False or True and False = ", $bool1 |  $bool2 & $bool1, "\n";
echo"True and True and (True or True) and False = ", $bool2 & $bool2 & ($bool2 | $bool2) & $bool1, "\n";
echo"True and True and not (True or True) and False = ", $bool2 & $bool2 & !($bool2 |  $bool2) & $bool1, "\n";
echo"True and True and True or True and False = ", $bool2 & $bool2 & $bool2 |  $bool2 & $bool1, "\n";
echo"True and not True and True or True and False = ", $bool2 & ! $bool2 & $bool2 |  $bool2 & $bool1, "\n";
echo("\n\n");

/*
4. Operator associativity rules for bool operators
all left associativity.
*/
echo("4. Operator associativity rules for bool operator \n\n");
echo"True and True and False => ", $bool2 & $bool2 & $bool1, "\n";
echo"True or True or False => ",    $bool2 | $bool2 | $bool1, "\n";
echo("\n\n");

/*
5. Operand evaluation order
LEFT -> RIGHT in php
*/
echo("5. Operand evaluation order \n\n");
echo "myfunction1() and myfunction2() and myfunction3() = ", myfunction1() & myfunction2() & myfunction3(), "\n";
echo "myfunction1() or myfunction2() or myfunction3() = ", myfunction1() | myfunction2() | myfunction3(), "\n";
echo "myfunction1() or myfunction2() and myfunction3() = ", (myfunction1() | myfunction2()) & myfunction3(), "\n";
echo("\n\n");

/*
6. short-circuit evoluation
LEFT -> RIGHT in c
*/
echo("6. short-circuit evoluation \n\n");
echo("These exapmles shows that php has not got short circuit \n");
echo "myfunction1() and myfunction2() and myfunction3() = ", myfunction1() & myfunction2() & myfunction3(), "\n";
echo "myfunction1() or myfunction2() or myfunction3() = ", myfunction1() | myfunction2() | myfunction3(), "\n";
echo "myfunction1() or myfunction2() and myfunction3() = ", (myfunction1() | myfunction2()) & myfunction3(), "\n";
echo("\n\n");

?>