age=input("How old are you?")

try:
    age=int(age)
    if age <=0:
        raise ValueError("Age cannot be negative.")
    print(f"You are {age} years old.")
except ValueError as ve:
    print(f"Error: {ve}")
finally:
    print("Thank you for providing your age.")