def task2(temperature,sign):
    celsius=(temperature-32)*5/9
    fahrenheit=(temperature*9/5)+32
    sign=sign.lower()
    return f'The given fahrenheit {temperature} in celsius is : {celsius:.2f}' if sign=='f' \
    else f'The given celsius {temperature} in celsius is : {fahrenheit:.2f}' if sign=='c' \
    else f'enter a correct sign, {sign} is invalid '
input2=float(input("Enter the temperature in celsius or farhenheit : "))
sign=input("Enter the sign : ")
print(task2(input2,sign))