        # 1)
def double_char(s):
            result = ""
            for i in s:
                result += i * 2
            return result
        # 1.1)
def get_average(marks):
    result = sum(marks) // len(marks)
    return result