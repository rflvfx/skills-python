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
- Document usage — iteration 36 (2015)
- Polish code — iteration 40 (2015)
- Fix lint warnings — iteration 45 (2015)
- Update dependencies — iteration 50 (2015)
- Fix typo — iteration 52 (2015)
- Extend coverage — iteration 1 (2016)
- Add example — iteration 4 (2016)
- Update config — iteration 8 (2016)
- Optimize performance — iteration 9 (2016)
- Tweak implementation — iteration 11 (2016)
- Improve error handling — iteration 14 (2016)
- Fix lint warnings — iteration 23 (2016)
- Document usage — iteration 28 (2016)
- Improve error handling — iteration 33 (2016)
- Improve error handling — iteration 46 (2016)
- Improve naming — iteration 51 (2016)
- Improve error handling — iteration 52 (2016)
