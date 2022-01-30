# 546A - Soldier and Bananas

ints = [int(i) for i in input().split()]

cost = 0
for i in range(1, ints[2] + 1):
    cost += i * ints[0]

if cost < ints[1]:
    print(0)
else:
    print(abs(ints[1] - cost))
