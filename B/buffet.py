n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
cnt = 0
index = -1

for i in a_list:
  cnt += b_list[i-1]
  if i == index+1:
    cnt += c_list[index-1]
  index = i
print(cnt)