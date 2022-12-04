from decimal import Decimal, ROUND_HALF_UP
x,k = map(int, input().split())

for i in range(1, k+1):
  x = Decimal(str(x)).quantize(Decimal(f'1E{i}'), rounding=ROUND_HALF_UP)
print(int(x))