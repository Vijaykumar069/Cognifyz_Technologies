def task4(input):
    a=[0,1]
    if input<0:
        return []
    elif input==1:
        return a[0]
    else :
        for i in range(2,input):
            a.append(a[-1]+a[-2])
    return a
input_interger=int(input("Enter a number to generate a range of Fibonacci series : "))
print(task4(input_interger))