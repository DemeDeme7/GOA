# 1. Remove String Spaces
def remove_string_spaces(x):
    return x.replace(' ', '')

# 2. Square(n) Sum
def square_n_sum(numbers):
    return sum(n ** 2 for n in numbers)

# 3. Count of positives / sum of negatives
def count_positives_and_sum_negatives(arr):
    if not arr:
        return []
    positives = sum(1 for x in arr if x > 0)
    negatives = sum(x for x in arr if x < 0)
    return [positives, negatives]

# 4. Abbreviate a Two Word Name
def abbreviate_name(name):
    return '.'.join([n[0].upper() for n in name.split()])

# 5. Convert a Number to a String!
def number_to_string_custom(num):
    return str(num)

# 6. Is he gonna survive? (hero-bullets)
def hero_survive(bullets, dragons):
    return bullets >= dragons * 2

# 7. Simple multiplication
def simple_multiplication_custom(number):
    return number * 8 if number % 2 == 0 else number * 9

# 8. Century From Year
def century_from_year(year):
    return (year + 99) // 100

# 9. Basic Mathematical Operations
def basic_math_op(operator, value1, value2):
    return eval(f"{value1}{operator}{value2}")

# 10. Fake Binary
def fake_binary(x):
    return ''.join('0' if int(c) < 5 else '1' for c in x)
