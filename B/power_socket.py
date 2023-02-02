a,b = map(int, input().split())
cnt = 0

while b > 1:
  b -= a-1
  cnt += 1
print(cnt)
