#include <stdio.h>
int main()
{
    long nc = 0;
    //python3 [i for i in '输入一段文字，输出总字符数'.encode('GB2312')]
    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c:",202, 228, 200, 235, 210, 187, 182, 206, 206, 196, 215, 214, 163, 172, 202, 228, 179, 246, 215, 220, 215, 214, 183, 251, 202, 253);
    while(getchar() != '\n')
    ++nc;
    printf("%ld\n",nc);
    return 0;
}