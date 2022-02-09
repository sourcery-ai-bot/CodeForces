# 546A - Soldier and Bananas

ints = [int(i) for i in input().split()]

cost = sum(i * ints[0] for i in range(1, ints[2] + 1))
if cost < ints[1]:
    print(0)
else:
    print(abs(ints[1] - cost))
