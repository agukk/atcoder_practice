#include <stdio.h>
#include <string.h>

int main(void)
{
  char s[104];
  int cnt = 0;
  scanf("%s", s);
  
  for (int i = 0; i < strlen(s)/2; i++)
  {
    if (s[i] != s[strlen(s)-i-1])
    {
      cnt += 1;
    }
  }
  
  printf("%d\n", cnt);
  return 0;
}