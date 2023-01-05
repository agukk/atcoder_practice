a, b, c, d = map(int, input().split())
blue_ball = a
red_ball = 0
ans = 0

while(True):
  blue_ball += b
  red_ball += c
  ans += 1
  if blue_ball / red_ball <= d:
    print(ans)
    break
  elif blue_ball > red_ball * d and b >= c * d:
    print(-1)
    exit()