# Problem 2
# http://projecteuler.net/index.php?section=problems&id=2
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#

def fibonacci(a = -1, b = 1, max = 4000000):
  while a + b < max:
    a, b = b, a + b
    yield b

print sum(i for i in fibonacci() if not i % 2)

# result: 4613732
