n = int(input())
d_list = list(map(int, input().split()))
cnt = 0

for i in range(n):
  for j in range(n):
    if i < j:
      cnt += d_list[i] * d_list[j]
print(cnt)