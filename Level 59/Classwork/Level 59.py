# 1)
def count_positives_sum_negatives (arr):
    return [sum(x > 0 for x in arr), sum(x for x in arr if x < 0)] if arr else []
# 2)
def are_you_playing_banjo(name): 
    if name[0].lower() == 'r':
        return name + "plays banjo"
    else:
        return name + "does not play banjo"
# 3)
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9
# 4) 
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result
# 5)
def disemvowel(string_):
    for vowel in "aeiouAEIOU":
        sting_ = string_.replace(vowel, "")
    return string_
# 6)
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
