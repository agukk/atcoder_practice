#include <stdio.h>

int main(void)
{
  // 変数
  long a, b, r, x, tmp;
  scanf("%ld%ld", &a, &b);
  x = a * b;
 
  /* 自然数 a > b を確認・入替 */
  if(a<b){
    tmp = a;
    a = b;
    b = tmp;
  }
 
  /* ユークリッドの互除法 */
  r = a % b;
  while(r!=0){
    a = b;
    b = r;
    r = a % b;
  }
 
  /* 最小公倍数を出力 */
  printf("%ld\n", x/b);
 
  return 0;

}