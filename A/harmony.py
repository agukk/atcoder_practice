a,b = map(int, input().split())
if (b - a) % 2 == 1:
  print('IMPOSSIBLE')
else:
  k = (b - a) // 2
  print(a+k)
