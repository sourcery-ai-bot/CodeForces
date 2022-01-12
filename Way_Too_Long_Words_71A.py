# 71A - Way Too Long Words

too_long = int(input())
for i in range(0, too_long):
  in_word = input()
  if len(in_word) > 10:
    in_word = in_word[0] + str(len(in_word) - 2) + in_word[-1]
  print(in_word)
