'''Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}'''


a = input("Enter Word To Count Word Frequency::")
b = {}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
