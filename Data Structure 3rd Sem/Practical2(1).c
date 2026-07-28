// Practical 2.1 : Write a program to prints array elements in reverse orders using pointers.

#include <stdio.h>
int main()
{
    int arr[5] = {10, 20, 30, 40,50};
    int *ptr = arr;

    for(int i = 4; i>=0; i--)
    {
        printf("%d\n", *(ptr+i));
    }
    
} 
