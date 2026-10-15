while
    try:
        number = input("Enter a number: ")
        break
    except StopIteration:
        raise ValueError("No input provided.")