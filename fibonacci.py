fib=[0,1]
n=10
for i in range(n):
    fib.append(fib[i]+fib[i+1])
print(fib)
