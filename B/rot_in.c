#include <stdio.h>
#include <string.h>

int main(void)
{
  int n;
  char s[10008];
  
  scanf("%d%s", &n, s);
  for (int i = 0; i < strlen(s); i++)
  {
    s[i] += n;
    if (s[i] > 90)
    {
      s[i] -= 26;
      printf("%c", s[i]);
      
    }
    else
    {
      printf("%c", s[i]);
    }
  }
  return 0;
}