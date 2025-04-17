# 1)
def min_max(lst):
  return [min(lst), max(lst)]
# 2)
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
# 3)
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
# 4)
def fizzbuzz(n):
    return [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        i
        for i in range(1, n + 1)
    ]
# 5)