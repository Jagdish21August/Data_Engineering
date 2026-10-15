vowels=['a','e','i','o','u']
word=input("Enter a word: ")
count=0
for letter in word:
    if letter not in vowels:
        count+=1
print(f"The number of consonants in '{word}' is: {count}")  