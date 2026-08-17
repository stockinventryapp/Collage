#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int stack[10], top = -1, val;
void display();
void push(int val);
void pop();
void peek();

int main()
{
    int choice;
    bool running = true;
    printf("1.Push\n2. Pop\n3. Peek\n4. Display\n5. Exit\n");
    while (running)
    {
        printf("Enter the choice : ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("Enter the value to push: ");
            scanf("%d", &val);
            push(val);
            break;
        case 2:
            pop();
            break;
        case 3:
            peek();
            break;
        case 4:
            display();
            break;
        case 5:
            running = false;
            break;
        default:
            printf("Invalid choice\n");
        }
    }

    return 0;
}

void display()
{
    if (top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Stack elements are: ");
        for (int i = top; i >= 0; i--)
        {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

void push(int val)
{
    if (top == 9)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        top++;
        stack[top] = val;
    }
    display();
}

void pop()
{
    if (top == -1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        printf("Popped element is: %d\n", stack[top]);
        top--;
    }
    display();
}

void peek()
{
    if (top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Top element is: %d\n", stack[top]);
    }
}
