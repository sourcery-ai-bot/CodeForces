# 59A - Word

in_str = input()
ups = [i for i in in_str if i.isupper()]
lows = [i for i in in_str if i.islower()]
if len(ups) > len(lows):
    print(in_str.upper())
else:
    print(in_str.lower())
