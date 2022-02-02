# 791A - Bear and Big Brother

bears = [int(i) for i in input().split()]
years = 0
while bears[0] <= bears[1]:
    bears[0] *= 3
    bears[1] *= 2
    years += 1

print(years)
