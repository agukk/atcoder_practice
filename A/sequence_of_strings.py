n = int(input())
name_list = []
for i in range(n):
  name = input()
  name_list.append(name)

for name in reversed(name_list):
  print(name)