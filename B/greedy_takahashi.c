#include <stdio.h>

int main(void)
{
  long a, b, k, c;
  scanf("%ld%ld%ld", &a, &b, &k);
  
  c = a - k;
  if (c < 0)
  {
    if (b+c < 0)
    {
      printf("%ld %ld", 0, 0);
    }
    else
    {
      printf("%ld %ld", 0, b+c);
    }
  }
  else
  {
    printf("%ld %ld", c, b);
  }
}