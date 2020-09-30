int main()
{
    int val = 1;
    val =42;
    asm("int $3"); // set a breakpoint here
    val = 7;
    return 0;
}

