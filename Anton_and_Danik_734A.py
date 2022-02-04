	# 734A - Anton and Danik
  
games = int(input())
winners = input()

anton = winners.count('A')
danik = winners.count('D')

if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else:
    print('Friendship')
