a, b, c = map(int, input().split())
 
if c - b == b - a:
  print('Yes')
elif b - c == c - a:
  print('Yes')
elif c - a == a - b:
  print('Yes')
else:
  print('No')