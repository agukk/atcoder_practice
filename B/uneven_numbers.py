n = int(input())
cnt = 0
for i in range(1, n+1):
  str_i = str(i)
  if len(str_i) % 2 == 1:
    cnt += 1
print(cnt)