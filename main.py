def fibonacci_number(number):
    fib_sequence = [0, 1]
    first_num = 0
    next_num = 1

    for _ in range(number-2):
        result = first_num + next_num
        fib_sequence.append(result)
        first_num = next_num
        next_num = result

    print(fib_sequence)


fibonacci_number(6)


def fib_recursion(number):
    if number == 1 or number == 2:
        return 1
    return fib_recursion(number-1) + fib_recursion(number-2)


fib = fib_recursion(7)
print(fib)

