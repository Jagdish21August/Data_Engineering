word=input("Enter a word: ")
character=input("Enter a character to find its occurrence: ")
count=0
for i in word:
    if i==character:
        count+=1
print(f"The number of occurrence of '{character}' in '{word}' is: {count}")