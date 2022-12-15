import collections

n = int(input())
a_list = list(map(int, input().split()))
a_dict = collections.Counter(a_list)
a_dec_list = sorted(a_dict.items(), reverse=True)

for i in range(len(a_dict)):
  print(a_dec_list[i][1])

for i in range(n - len(set(a_list))):
  print(0)