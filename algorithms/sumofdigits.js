function sumOfDigits(num) {
    if (num == 0) {
        return 0;
    }
    return num % 10 + sumOfDigits(Math.floor(num / 10));
}

/*

How it works:

The num%10 returns the remainder of the number after divided by 10, e.g., 324 % 10 = 4
The Math.floor(num / 10) returns the whole part of the num / 10 e.g., Math.floor(324 / 10) = 32
The if(num == 0) is a condition that stops calling the function.

https://www.javascripttutorial.net/javascript-recursive-function/
*/