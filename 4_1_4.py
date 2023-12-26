from functools import cache

mem = {}
def fib_memo(n):
    if n < 0:
      return ('Введите число больше нуля!')
    if n in mem:
      return mem[n]
    if n == 0:
      result = 0
    elif n == 1:
      result = 1
    else:
      result = fib_memo(n - 1) + fib_memo(n - 2)
    mem[n] = result
    return result

@cache
def fibonacci(n):
    if n <= 1:
      return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fib_memo(10))
print(fibonacci(10))
