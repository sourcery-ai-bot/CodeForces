# 282A - Bit++

import math
raw = int(input())
x_val = 0
for _ in range(raw):
    in_str = input()
    if in_str in ["X++", "++X"]:
        x_val += 1
    elif in_str in ["--X", "X--"]:
        x_val -= 1
print(x_val)
