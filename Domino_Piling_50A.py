# 50A - Domino Piling

import math
raw = input().split()
m, n = int(raw[0]), int(raw[1])
area_size = m * n
print(math.floor(area_size / 2))
