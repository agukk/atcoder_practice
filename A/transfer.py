a,b,c = map(int, input().split())
d = a - b
if c - d >= 0:
  print(c-d)
else:
  print(0)