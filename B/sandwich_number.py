s = input()

if s[0].isalpha() and s[-1].isalpha() and len(s) == 8 and s[1:7].isdecimal() and s[1] != '0':
  print('Yes')
else:
  print('No')