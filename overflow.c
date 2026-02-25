#include <stdio.h>

int main()
{
    char buffer[8] = "hello";
    gets(buffer);
    printf("%s\n", buffer);
    return 0;
}
