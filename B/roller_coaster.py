n,k = map(int, input().split())
heights = list(map(int, input().split()))
cnt = 0

for height in heights:
  if height >= k:
    cnt += 1
print(cnt)