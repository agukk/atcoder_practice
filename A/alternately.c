#include <stdio.h>

int main()
{
    int n;
    char s[110];
    scanf("%d%s", &n, s);

    for (int i = 0; i < n - 1; i++)
    {
        if (s[i] == s[i+1])
        {
            printf("No\n");
            return 0;
        }
    }
    printf("Yes\n");
    return 0;
}