#include <stdio.h>

int main(void)
{
  int a, b, c;
  scanf("%d%d%d", &a, &b, &c);
  int total = a+b+c;
  
  if (total <= 21)
  {
    printf("win\n");
  }
  else
  {
    printf("bust\n");
  }
  return 0;
}