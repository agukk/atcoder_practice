#include <stdio.h>

int main(void)
{
  int a, b;
  scanf("%d%d", &a, &b);
  
  if (1<=a&&a<=9 && 1<=b&&b<=9)
    printf("%d", a*b);
  else
    printf("%d", -1);
  return 0;
}