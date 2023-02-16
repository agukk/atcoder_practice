n,k,q = map(int, input().split())
points = [k] * n

for i in range(q):
  c_a = int(input()) - 1
  points[c_a] += 1

for i in range(n):
  points[i] -= q
  if points[i] > 0:
    print('Yes')
  else:
    print('No')