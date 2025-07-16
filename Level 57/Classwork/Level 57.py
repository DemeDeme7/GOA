# 1. Round up to the next multiple of 5
def round_to_next5(n):
    return n if n % 5 == 0 else n + (5 - n % 5)

# 2. Fix the first character capitalization
def fix_capitalization(s):
    return s.capitalize()

# 3. Switch it Up! (Number to word)
def switch_it_up(number):
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return words[number]

# 4. Odd or Even? (Sum is odd or even)
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"
