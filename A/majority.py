n = int(input())
f = 0
a = 0
for i in range(n):
  if input() == 'For':
    f += 1
  else:
    a += 1

if f > a:
  print('Yes')
else:
  print('No')