#!/usr/bin/env python3

def fib_recursive(n):
    if n<= 0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_sequence = fib_recursive (n-1)
        fib_sequence.append(fib_sequence[-1]+ fib_sequence[-2])
        return fib_sequence
    
def print_fibonacci (length):
    fib_sequence = fib_recursive(length)
    print(fib_sequence)
print_fibonacci(9)