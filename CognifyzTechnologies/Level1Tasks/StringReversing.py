def task1(input):
    #we can also write it as ''.join(reversed(input)) & there are multiple ways to reverse a given string
    return ''.join(i for i in reversed(input)) 
input1=input("Enter any string : ")
print(task1(input1))
