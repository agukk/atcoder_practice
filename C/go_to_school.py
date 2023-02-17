n = int(input())
a_list = list(map(int, input().split()))
ans_list = [0] * n

for i, a in enumerate(a_list):
  ans_list[a-1] = i + 1
print(*ans_list)