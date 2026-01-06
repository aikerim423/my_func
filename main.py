def fib_recursion(number):
    if number == 1 or number == 2:
        return 1
    return fib_recursion(number-1) + fib_recursion(number-2)


fib = fib_recursion(7)
print(fib)
