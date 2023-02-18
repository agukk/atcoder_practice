#include <stdio.h>

int main(void)
{
  int n;
  scanf("%d", &n);
  int i,j;
  for (i=1; i<10; i++)
  {
    for (j=1; j<10; j++)
    {
      if (n == i*j)
      {
        printf("Yes\n");
        return 0;
      }
    }
  }
    
  printf("No\n");
  return 0;
}