def is_valid_palindrome(input):
    # THERE ARE MANY WAYS TO CHECK WHEATHER A GIVEN STRING IS PALINDROME OR NOT 
      input=input.lower()
      return f'{input} is a Palindrome' if input==input[::-1] else f'{input} is not a Palindrome'
input1=input("Enter any string : ")
print(is_valid_palindrome(input1))