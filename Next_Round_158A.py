# 158A - Next Round

raw = input().split()
n, k = int(raw[0]), int(raw[1])
places = input().split()
passing_val = int(places[k - 1])
valid_places = [p for p in places if p != "0" and int(p) >= passing_val]
print(len(valid_places))
