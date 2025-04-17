# 1)    
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = []
    for i in string_:
        if i not in vowels:
            result.append(i)
    return ''.join(result)
# 2)
    def high_and_low(numbers):
        numbers_list = [int(i) for i in numbers.split()]
        highest = numbers_list[0]
        lowest = numbers_list[0]
        
        for i in numbers_list:
            if i > highest:
                highest = i
            if i < lowest:
                lowest = i
        
    
    return str(highest) + " " + str(lowest)
# 3)
def square_digits(num):
    digits = str(num)
    squared_digits = []
    for digit in digits:
        squared_digits.append(str(int(digit) ** 2))
    return int(''.join(squared_digits))