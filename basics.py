# Python fundamentals
squares = [n**2 for n in range(10)]
evens = [n for n in range(20) if n % 2 == 0]

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(squares, evens, fib(10))
- Add helper — iteration 4 (2015)
