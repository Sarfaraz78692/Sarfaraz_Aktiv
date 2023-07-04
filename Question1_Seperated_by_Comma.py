'''Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 50, 25, 17, 3
Output :
List : ['50, ' 25', ' 17', ' 3']
Tuple : ('50', ' 25', ' 17', ' 3')'''

user_input = input("Enter A Number::")
user_input = user_input.split(",")
print(user_input)
user_input = tuple(user_input)
print(user_input)

