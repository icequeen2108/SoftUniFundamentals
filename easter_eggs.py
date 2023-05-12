import re

data = input()
pattern = r'(@{1,}|#{1,})([a-z]{3,})(@|#{1,})\D+([0-9]{1,})'
result = re.findall(pattern, data)

for itr in range(len(result)):
    amount = result[itr][3]
    colour = result[itr][1]
    print(f"You found {amount} {colour} eggs!")