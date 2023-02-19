#include <stdio.h>
#include <string.h>

int main(void)
{
  char s[10];
  scanf("%s", s);
  
  char *days[] = {"SAT", "FRI", "THU", "WED", "TUE", "MON", "SUN"};
  for (int i = 0; i < 7; i++)
  {
    if (strcmp(s, days[i]) == 0)
    {
      printf("%d\n", i+1);
      return 0;
    }
  }
}