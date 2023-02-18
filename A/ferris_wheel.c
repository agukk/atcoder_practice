#include <stdio.h>

int main()
{
  int a,b;
  scanf("%d%d", &a, &b);
  if (a >= 13){
    printf("%d", b);
  } else if (a >= 6 && a <= 12){
    printf("%d", b/2);
  } else {
    printf("0");
  }
}