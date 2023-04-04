#include <stdio.h>

int main(void)
{
  char s[9][9];
  int line[] = {8, 7, 6, 5, 4, 3, 2, 1};
  char column[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};
  
  for (int i = 0; i < 8; i++)
  {
      scanf("%8s", s[i]);
  }
  
  for (int i = 0; i < 8; i++)
  {
    for (int j = 0; j < 8; j++)
    {
      if (s[i][j] == '*')
      {
        printf("%c%d\n", column[j], line[i]);
      }
    }
  }
}