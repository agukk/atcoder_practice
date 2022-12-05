h, w = map(int, input().split())

cnt = 0
for i in range(h):
  cnt += input().count('#')

print(cnt)