k,x = map(int, input().split())
b = x-(k-1)
e = x+k

while b < e:
  print(b, end=' ')
  b += 1