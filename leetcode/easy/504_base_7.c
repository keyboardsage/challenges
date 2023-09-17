int base10ToBaseN(int num, size_t radix) {
    size_t remainder = 0;
    size_t accumulator = 0;
    int the_sign = (num < 0) ? -1 : 1;

    num *= the_sign; // ensure num is positive for now

    for (int i = 0; num != 0; i++) {
        // calculate the number
        remainder = num % radix;
        num = num / radix;

        // set up a base 10 integer
        accumulator += pow(10, i)*remainder;
    }

    return accumulator * the_sign;
}

char * convertToBase7(int num){
    // create a 10 character string, no conversion from base 10 to base 7 will be larger
    // than 9 characters when -10**7 < num < 10**7, plus one more character for negative sign
    char* returnValue = (char*)malloc(11 * sizeof(char));
    returnValue[10] = '\0';

    sprintf(returnValue, "%d", base10ToBaseN(num, 7));

    return returnValue;
}