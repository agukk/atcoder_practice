n = int(input())
total_nuts = 0
a_list = list(map(int, input().split()))

for i in range(n):
  if a_list[i] > 10:
    harvested_nuts = a_list[i] - 10
    total_nuts += harvested_nuts
print(total_nuts)