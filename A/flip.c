#include <stdio.h>

int main(void)
{
  char s[12];
  scanf("%s", s);
  int i;
  for(i = 0; s[i] != '\0'; i++)
  {
    if (s[i] == '0')
      s[i] = '1';
    else
      s[i] = '0';
  }
  printf("%s", s);
}
