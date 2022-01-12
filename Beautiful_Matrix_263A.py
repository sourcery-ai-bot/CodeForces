# 263A - Beautiful Matrix

a = input().split()
b = input().split()
c = input().split()
d = input().split()
e = input().split()

def print_solution(col, row):
    print(abs(3 - col) + abs(3 - (row + 1)))

if "1" in a:
    print_solution(1, a.index("1"))
elif "1" in b:
    print_solution(2, b.index("1"))
elif "1" in c:
    print_solution(3, c.index("1"))
elif "1" in d:
    print_solution(4, d.index("1"))
elif "1" in e:
    print_solution(5, e.index("1"))
