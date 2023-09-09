def task1():
    import random as r
    computer=r.randint(1,100)
    while True:
        # print("Computer number is : ",computer)
        user=int(input("Enter a number : "))
        if user<computer:
            print("Too low")
        elif user>computer:
            print("Too high")
        elif user==computer:
            print(f"correct!!! {computer}-computer number and {user}-user number are equal...")
            break
task1()