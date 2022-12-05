n = int(input())
s_list = list(map(int, input().split()))

ans_list = []
for i in range(1, n):
  num = s_list[i] - s_list[i-1]
  ans_list.append(num)

s = [str(a) for a in ans_list]
s = " ".join(s)
print(str(s_list[0])+ " " + s)