# 118A - String Task

a = list(input().lower().replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("y", ""))
pr_str = ""
if len(a) > 0:
    for e in a:
        pr_str += "." + e
print(pr_str)
