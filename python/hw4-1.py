import sys

def fibonacci_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

input_n = int(sys.argv[1])
print(fibonacci_rec(input_n))