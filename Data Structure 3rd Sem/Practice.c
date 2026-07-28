#include <stdio.h>

int main()
{
    int i=5;
    int *ptr = &i;

    printf("Value of variable : %d\n",i);
    printf("Value of variable : %d\n",&i);
    printf("Address of variable : %p\n",&i);
    printf("Value of variable using pointer : %d\n",*ptr);
    printf("Address of variable : %p\n",ptr);
}
