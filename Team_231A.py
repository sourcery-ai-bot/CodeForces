# 231A - Team

lines = int(input())
implement = 0
for _ in range(lines):
  raw_given = input().split()
  p, v, t = int(raw_given[0]), int(raw_given[1]), int(raw_given[2])
  if p + v + t > 1: implement += 1
print(implement)
