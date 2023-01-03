n = int(input())
day = 0

while(True):
  day += 1
  if 1/2*day*(day + 1) >= n:
    print(day)
    break
