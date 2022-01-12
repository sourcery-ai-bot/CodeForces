# 112A - Petya and Strings

a = input().lower()
b = input().lower()
ab_list = sorted([a, b])

if a == b:
    print("0")
else:
    if ab_list.index(a) == 0:
        print("-1")
    elif ab_list.index(a) == 1:
        print("1")
