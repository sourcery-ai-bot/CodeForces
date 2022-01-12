# 282A - Bit++

import math
raw = int(input())
x_val = 0
for i in range(0, raw):
    in_str = input()
    if in_str == "X++" or in_str == "++X":
        x_val += 1
    elif in_str == "--X" or in_str == "X--":
        x_val -= 1
print(x_val)
