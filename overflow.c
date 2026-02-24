#include <stdio.h>

int main()
{
    char buffer[8] = "hi";
    gets(buffer);
    printf("%s\n", buffer);
    return 0;
}
