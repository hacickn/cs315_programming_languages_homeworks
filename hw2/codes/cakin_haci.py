# 1. Iteration statements provided
# Iterations are provided in python by using while, for and nested loops

print("1. Iteration statements provided \n ")
check = True
number1 = 0

print("while loop")
while(check):
    if(number1 == 3):
        print("Reached to 3 \n")
        check = False
        break
    print(number1)
    number1 += 1


print("for loop")
for i in range (1,10):
    if(i == 5):
        print("Reached to 5 \n")
        break 
    print(i)

print("nested loop")
for i in range (1,5):
    for j in range(2,3):
        print(i , " * ", j ," = ", i*j )


# 2. Data structures suitable for iteration
# Built in data structures are in python set, tuple, dictionary, enumerate and list
print("\n2. Data structures suitable for iteration \n ")

print("For Tupple")
tupple = ("23","haci",("halil","altay"))
for i in tupple:
    print(i)

print(" \nFor List")
list1 = ["23","haci",["halil","altay"]]
for i in range (0,3):
    print (list1[i])

print(" \nFor Dictonary")
dictionary = {"age":23,"name":"haci","dep":"cs"}
for i in dictionary:
    print(dictionary[i])

print(" \nFor Set")
set1 = {"23","haci","cs"}
for i in set1:
    print(i)

print(" \nFor Enumerate")
for key, value in enumerate(['cs', '315', 'bilkent', 'Atalar']):
    print(key, value)

# 3. The way the next item is accessed
print("\n3. The way the next item is accessed \n ")
number2 = 0
print("for")
while( number2 < 10 ):
    print("number2 = " , number2)
    number2 = number2 + 2

print("\nfor/in")
for number3 in range (0,10):
    print("number3 = ", number3)
    number3 = number3 + 3