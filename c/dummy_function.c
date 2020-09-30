#include <stdlib.h>

void dummy_function() {
    int* x = malloc(10 * sizeof(int));
    x[10] = 0;
}

int main()
{
    dummy_function();
    return 0;
}
