N = int(input())

Alice_points = 0
Bob_points = 0

not_sorted_list = list(map(int, input().split()))
sorted_list = sorted(not_sorted_list, reverse=True)

for i in range(0, N, 2):
  Alice_points += sorted_list[i]

for j in range(1, N, 2):
  Bob_points += sorted_list[j]

required_ans = Alice_points - Bob_points

print(required_ans)