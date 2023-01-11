n,a,x,y = map(int, input().split())
price = 0

for i in range(1, n+1):
  if i > a:
    price += y
  else:
    price += x
print(price)