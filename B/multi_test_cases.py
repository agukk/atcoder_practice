t = int(input())

for i in range(t):
  n = int(input())
  cnt = 0
  a_list = list(map(int, input().split()))
  for num in a_list:
    if num % 2 == 1:
      cnt += 1
  print(cnt)    
      