h,w = map(int, input().split())
lists = [list(input()) for i in range(h)]
ans_list = [0 for i in range(w)]

for width in range(w):
  for height in range(h):
    if lists[height][width] == '#':
      ans_list[width] += 1

for i in range(w):
    # print(ans_list[i])だと改行してしまうから、end=' 'で改行を防ぎ１字空けるように設定
    print(ans_list[i], end=' ')