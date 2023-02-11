n = int(input())
h_list = list(map(int, input().split()))
cnt = 0
ans = 0

for i in range(1, n):
  if h_list[i-1] >= h_list[i]:
    cnt += 1
  else:
    cnt = 0
  ans = max(ans, cnt)
  
print(ans)