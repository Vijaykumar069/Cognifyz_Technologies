def task4(a,b,sign):
     return f'The sum of {a} and {b} is {a+b}' if sign=="+" else \
            f'The difference of {a} and {b} is {a-b}' if sign=="-" else \
            f'The multipliaction of {a} and {b} is {a*b}' if sign=="*" else \
            f'The modulus of {a} and {b} is {a%b}' if sign=="%" else \
            f'The division of {a} and {b} is {a/b}' if sign=="/" else \
            f'{sign} is an invalid sign'
            
       
input1,input2=map(float,input("enter the value of a and b : ").split())
sign=input("enter the sign(+,-,*,%,/) : ")
print(task4(input1,input2,sign))