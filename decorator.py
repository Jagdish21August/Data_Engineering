import time
def brew_tea():
    time.sleep(5)
    print("Tea is ready!")

 
def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Time taken to brew tea: {end_time - start_time:.2f} seconds")
    return wrapper

brew_tea = timer_decorator(brew_tea)
brew_tea()