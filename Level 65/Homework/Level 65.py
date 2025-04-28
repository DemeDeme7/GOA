# 1) List Filtering
def filter_list(l):
    return [i for i in l if type(i) == int]
# 2) Jaden Casing Strings
def to_jaden_case(strg):
    return ' '.join(word.capitalize() for word in strg.split())
# 3) Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
# 4) Is this a triangle?
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
# 5) Two to One
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
# 6) Get the Middle Character
def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]
# 7) Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
# 8) Disemvowel Trolls
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return ''.join(i for i in string_ if i not in vowels)
# 9) Highest and Lowest
def high_and_low(numbers):
    numbers_list = [int(i) for i in numbers.split()]
    return str(max(numbers_list)) + " " + str(min(numbers_list))
# 10) Complementary DNA
def DNA_strand(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[i] for i in dna)