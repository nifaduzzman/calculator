#calculator
def add(a,b) :
    return a + b

def dif (a,b) :
    return a-b

def mul(a,b) :
    return a*b

def divide(a,b):
    return a/b


number1 = int(input('Enter the first number:'))
Input_operator = input('Please Enter what a operator:')
number2 = int(input('Enter the second number:'))

if Input_operator == '+' :
    print('Your given two numbers summation is:' , add(number1,number2))
elif Input_operator == '-' :
    print('Your given two numbers differation is :' , dif(number1,number2))
elif Input_operator == '*' :
    print('Your given two numbers multiplication is:' , mul(number1,number2))
elif Input_operator == '/' :
    print('Your given two numbers divide is:' , divide(number1,number2))