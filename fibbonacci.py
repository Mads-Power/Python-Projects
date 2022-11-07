
# this functions generates the Fibonacci numbers with the help og Yield
def fib(num):
    # Fibonacci starts with 0 the 1 ..1 ..2 ..3 etc 
    # multyplaing the two last numbers to create the next number
    a = 0
    b = 1
    for i in range(num):
        # since Fibonaccy can take up a lot of space in memory we use
        # Yield, it is used like a return, but the function will return a generator
        # Generators will run once. they forget about the last number calculated.
        
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(21):
    print(x)