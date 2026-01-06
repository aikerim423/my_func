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