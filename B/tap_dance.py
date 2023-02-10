s = input()

for i, s_c in enumerate(s):
  if i % 2 == 1 and s_c == 'R':
    print('No')
    break
  elif i % 2 == 0 and s_c == 'L':
    print('No')
    break
  elif i+1 == len(s):
    print('Yes')