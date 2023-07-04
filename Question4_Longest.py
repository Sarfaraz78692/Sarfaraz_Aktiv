#Write a Python function that takes a list of words and return the longest word and the length of the longest one.

'''a = ['saif','faiz','Zoyas','Sarfaraz','aryan','Fai zalarab']
a.sort() 
print(a)
print(max(a))
#print(a[0])
print(len(a[0]))'''

def longest_word():
    n = int(input("Enter The Words in Add the List: "))
    empty = []

    for i in range(n):
        add_word = input("enter words: ")
        empty.append(add_word)


    print("The Entered List is: ", empty)
    print("Longest Word of List: ", min(empty))
    print("Longest Word in List is: ", len(min(empty)))


longest_word()
        
