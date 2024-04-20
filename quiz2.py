""""Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100"""
a, b = 0, 1
fib_sequence = [a]

while b <= 100:
    fib_sequence.append(b)
    a, b = b, a + b

print("Fibonacci sequence up to 100:")
print(fib_sequence)
