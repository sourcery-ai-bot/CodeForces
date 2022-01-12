# 1A - Theatre Square

import math
raw_given = input().split()
n, m, a, = int(raw_given[0]), int(raw_given[1]), int(raw_given[2])
print(int(math.ceil(n / a)) * int(math.ceil(m / a)))
