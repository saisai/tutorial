// C program to demonstrate that array elements are stored 
// contiguous locations 

#include <stdio.h>
int main() {
       // an array of 10 integers.  If arr[0] is stored at 
    // address x, then arr[1] is stored at x + sizeof(int) 
    // arr[2] is stored at x + sizeof(int) + sizeof(int) 
    // and so on. 

    int arr[5], i;

    printf("Size of integer in this compiler is %lu\n", sizeof(int));

    for (i = 0; i < 5; i++)
    {
        // the use of '&' before a variable name, yields
        // address of ariable
        printf("Address arr[%d] is %p\n", i, &arr[i]);
    }

    return 0;
}
