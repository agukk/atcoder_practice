n, pocket = map(int, input().split())
a_list = list(map(int, input().split()))
discount = n / 2
total_price = sum(a_list) - discount

if pocket >= total_price:
  print('Yes')
else:
  print('No')