bool1 = False
bool2 = True
int1 = 2
int2 = 5
float1 = 2.3
float2 = 2.6
string1 = "haci"
string2 = "ilke"
complex1 = 1j
complex2 = 2j

# 1. Boolean Operators Provided ( and, or, not)
print("*********************************************************") 
print("1. Boolean Operators Provided  **************************")
print("*********************************************************")
print("and, or, not")
print("\n")

# 2. Data types for operands of boolean operators
print("*********************************************************")
print("2. Data types for operands of boolean operators *********")
print("*********************************************************")
print("\n")

# for "and" operator
print("=> And Operator******************************************")
print("false and true => " , bool1 and bool2) 
print("2 and 5 => ", int1 and int2)
print("haci and ilke => ", string1 and string2),
print("1j and 2j => ", float1 and float2)
# print("2.3 and 2.6 => ", complex1 and complex1") # do no support
print("\n")

# for "or" operator
print("=> Or Operator  *****************************************")
print("false or true => " ,bool1 or bool2)  
print("2 or 5 => ", int1 or int2)
print("haci or ilke => ", string1 or string2),
print("1j or 2j => ", float1 or float2)

# print("2.3 or 2.6 => ", complex1 or complex1") # do no support
print("\n")

# for ==
print("=> ==  Operator  ***************************************")
print("false == true => " , bool1 == bool2) 
print("2 == 5 => ", int1 == int2)
print("haci == ilke => ", string1 == string2)
print("2.3 == 2.6 => ", float1 == float2)
print("1j == 2j => ", complex1 == complex2) 
print("\n")
print("false == false => " , bool1 == bool1) 
print("2 == 2 => ", int1 == int1)
print("haci == haci => ", string1 == string1)
print("2.3 == 2.3 => ", float1 == float1)
print("1j == 1j => ", complex1 == complex1) 

print("\n")

# for "not"
print("=> not Operator  *****************************************")
print("false and not true => ", bool1 and not (bool2)) # false
print("not 5 => ", not int2)
print("not haci  => ", not string1)
print("not 2.3 => ", not float1)
print("false or not true => ",bool1 or not bool2) # false
print("2 and not 5 => ", int1 and not int2) # false
print("2 or not 5 => ", int1 or not int2) # 2
print("not haci => ", not string1)
print("\n")

# 3. Operator precedence rules in descending order
# 1 --> ()     
# 2 --> not     
# 3 --> and 
# 4 --> or    

print("*********************************************************")
print("3 Operator precedence rules in descending order for boolean operator *********")
print("*********************************************************")
print("1 --> ()") 
print("2 --> not") 
print("3 --> and")
print("4 --> or ")
print("\n")

print("True and True or False = ", True and True or False)
print("True or True and False = ", True or True and False)
print("False or True and False = ", False or True and False)
print("False or True and False = ", False or True and False)
print("True and True and (True or True) and False = ", True and True and (True or True) and False)
print("True and True or not (True or True) and False = ", True or True and not (True or True) and False)
print("True and True and True or True and False = ", True and True and True or True and False)
print("True and not True and True or True and False = ", True and not True and True or True and False)
print("\n")

# 4 Operator associativity rules for bool operators
# 1 --> and, or, == , != ---> left associativity.
print("*********************************************************")
print("4 Operator associativity rules for bool operators *******")
print("*********************************************************")
print("1 --> and ---> left associativity.")
print("2 --> or  ---> left associativity.")
print("3 --> ==  ---> left associativity.")
print("4 --> !=  ---> left associativity.")
print("\n")

print("True and True and False = ")
print( True and True and False )
print("True or True or False = ")
print( True or True or False)
print("True == True == False")
print( True == True == False)
print("True != True != False = ")
print(True != True != False )
print("\n")

# 5 Operand evaluation order
# left to right order
print("*********************************************************")
print("5 Operand evaluation order for bool operators ***********")
print("*********************************************************")
print("\n")
def myfunction1():
    print("1. function")  
    return False

def myfunction2():
    print("2. function")  
    return True  

def myfunction3():
    print("3. function")  
    return False  


print("\n")

# 6 Short-circuit evaluation
# Python has short circuit for and, or
print("\n")
print("*********************************************************")
print("6 Short-circuit evaluation ******************************")
print("*********************************************************")
print("These examples show that python has short circuit")
print("For and, if python face with false operand, python do not check rest of the expression")
print("For or, if python face with true operand, python do not check rest of the expression")
print("\n")

print("myfunction1() and myfunction2() and myfunction3() = ")
print( myfunction1() and myfunction2() and myfunction3())
print("myfunction1() or myfunction2() or myfunction3() = ")
print( myfunction1() or myfunction2() or myfunction3())
print("myfunction1() == myfunction2() == myfunction3() = ")
print( myfunction1() == myfunction2() == myfunction3())
print("myfunction1() != myfunction2() != myfunction3() = ")
print( myfunction1() != myfunction2() != myfunction3())