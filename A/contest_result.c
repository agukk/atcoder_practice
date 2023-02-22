#include <stdio.h>

int main(void)
{
  int n, m;
  scanf("%d%d", &n, &m);
  int a[n+1];
  int b[m+1];
  int total = 0;
  
  for (int i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
  }
  for (int j = 0; j < m; j++)
  {
    scanf("%d", &b[j]);
    total += a[b[j]-1]; 
  }
  printf("%d\n", total);
  return 0;
}