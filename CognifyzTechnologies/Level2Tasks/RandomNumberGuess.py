import random
def task2(lower_limit,upper_limit):
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    while True:
        try:
            guessed_number = int(input("Enter your guess : "))
            attempts += 1
            if guessed_number < secret_number:
                print("Too low! Try again.")
            elif guessed_number > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts..")
                break
        except ValueError:
            print("Invalid input, Please enter a valid number..")

lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))
task2(lower_limit, upper_limit)
