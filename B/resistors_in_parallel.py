n = int(input())
a_list = list(map(int, input().split()))
ans = 0
for i in range(n):
  ans += 1/a_list[i]
print(1/ans)