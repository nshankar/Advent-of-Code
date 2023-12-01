# A rock X
# B paper Y
# C scissors Z

# This function assumes p != q
def wins(p, q):
    if p == 'A' and q == 'Y': return True
    if p == 'B' and q == 'Z': return True
    if p == 'C' and q == 'X': return True
    return False

score_dict = { 'X':1, 'Y':2, 'Z':3 }
with open("input.txt", encoding="utf-8") as f:
    data = [i for i in f.readlines()]
    score = 0
    for line in data:
        p,q = line.split()
        if ord(p) == ord(q)-23:
            score += 3
        elif wins(p,q):
            score += 6
        score += score_dict[q]
    print(score)

# Returns whether we should play A B C depending on what p,q are
def scoring_helper(p,q):
    if q == 'Y': return p
    if q == 'X':
        tmp = ord(p) - 1
        if tmp < 65: tmp += 3
        return chr(tmp)
    if q == 'Z':
        tmp = ord(p) + 1
        if tmp > 67: tmp -= 3
        return chr(tmp)

score_dict2 = { 'A':1, 'B':2, 'C':3 }
with open("input.txt", encoding="utf-8") as f:
    data = [i for i in f.readlines()]
    score = 0
    for line in data:
        p,q = line.split()
        move = scoring_helper(p,q)
        score += score_dict2[move]
        if q == 'Y':
            score += 3
        elif q == 'Z':
            score += 6
    print(score)
