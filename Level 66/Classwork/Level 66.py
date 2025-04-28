# 1)
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    else:
        return "Player 2 won!"
# 2)
def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
# 3)
    def to_alternating_case(string):
        return string.swapcase()    
# 4)
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += int(p0 * (percent / 100)) + aug
        years += 1
    return years
# 5)
# ?
# 6)

