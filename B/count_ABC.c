#include <stdio.h>

int main(void)
{
  int n;
  int cnt = 0;
  char s[52];
  scanf("%d%s", &n, s);
  
  for (int i = 0; i < n-2; i++)
  {
    if (s[i] == 'A' && s[i+1] == 'B' && s[i+2] == 'C')
    {
      cnt += 1;
    }
  }
  printf("%d\n", cnt);
  return 0;
}