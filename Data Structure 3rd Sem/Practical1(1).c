#include <stdio.h>

int main()
{
    // For insert the value in array at given position
    int arr[5] = {10, 20, 30, 40, 50};
    int n = 5;
    int pos = 2;
    int value = 25;

    /*for (int i = n; i > pos; i--)
    {
        arr[i] = arr[i - 1];
    }

    arr[pos] = value;
    n++;

    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }*/
  
    for (int i = n; i > pos; i++)
    {
        arr[i] = arr[i - 1];
    }

    
    n--;

    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }


}

