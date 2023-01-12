n = int(input())
s = input()

for index, num in enumerate(s):
  if index % 2 == 0 and num == '1':
    print('Takahashi')
    break
  elif index % 2 == 1 and num == '1':
    print('Aoki')
    break