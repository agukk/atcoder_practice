n, k = map(int, input().split())

for i in range(k):
  if int(n) % 200 == 0:
    n = int(n) // 200
  else:
    n = str(n) + '200'
    
print(n)