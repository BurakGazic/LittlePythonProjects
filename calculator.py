print("Calculator!!")

from functools import reduce
import operator

##Funcitons
def prod(x):
    return reduce(operator.mul, x)

def extr(x):
    return reduce(operator.sub, x)

def sect(x):
    return reduce(operator.truediv, x)

#INPUTS
number_size = int(input("Enter the nnumber size :"))

operand = int(input("Collection = 1 , Subtract = 2 , Multiply = 3 , Partition = 4 :)"))


#VARAIBLES
x = []
i = 0

#LOOP 
while i < number_size:
    x.append(int(input("Enter the " + str(i+1) + ". number :")))
     
    i += 1

#CONTEXT
if operand == str(operand):
    print("You must enter a integer value!!")

elif operand == 1:
    print(sum(x))
    
elif operand == 2:
    print(extr(x))

elif operand == 3:
    print(prod(x))

elif operand == 4:
    print(sect(x))
