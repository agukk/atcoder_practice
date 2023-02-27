#include <stdio.h>

int main(void)
{
  int n;
  char s[102];
  char t[102];
  scanf("%d%s%s", &n, s, t);
  
  for (int i = 0; i < n; i++)
  {
    printf("%c%c", s[i], t[i]);
  }
  return 0;
}