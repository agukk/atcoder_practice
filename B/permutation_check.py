n = int(input())
a_list = list(map(int, input().split()))

if len(a_list) == len(set(a_list)):
  print('Yes')
else:
  print('No')