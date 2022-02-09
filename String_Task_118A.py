# 118A - String Task

a = list(input().lower().replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("y", ""))
pr_str = ""
if a:
    for e in a:
        pr_str += f'.{e}'
print(pr_str)
