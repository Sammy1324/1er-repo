def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
n = 10  # Change this value to generate more or fewer Fibonacci numbers
print(fibonacci(n))