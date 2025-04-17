# 1)
def filter_list(l):
    return [item for item in l if type(item) == int]
# 2)
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
# 3)
def find_short(s):
    return min(len(word) for word in s.split())
# 4)
def friend(names):
    return [name for name in names if len(name) == 4]
# 5)
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
