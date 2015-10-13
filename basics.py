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
- Fix lint warnings — iteration 12 (2015)
- Add feature — iteration 13 (2015)
- Add tests — iteration 18 (2015)
- Add example — iteration 22 (2015)
- Update config — iteration 24 (2015)
- Improve error handling — iteration 25 (2015)
- Add feature — iteration 33 (2015)
- Update dependencies — iteration 35 (2015)
