typedef long long int size_tlli;

char* positivei_to_a(size_tlli n) {
    // determine the amount of memory needed
    size_tlli remainder;
    size_tlli indicesRequired = 0;
    size_tlli temp = n;
    for (; temp != 0 ; indicesRequired++) temp /= 10;

    // allocate it
    char* s = (char*)malloc((indicesRequired+1) * sizeof(char));
    s[indicesRequired] = '\0'; // NUL char for string termination

    // build the string
    const size_tlli START_ASCII_DIGITS = 48;
    for (size_tlli j = 0; j < indicesRequired; j++) {
        remainder = n % 10;
        n = n / 10;

        s[indicesRequired-j-1] = START_ASCII_DIGITS + remainder;
    }

    return s;
}

int reverse(int x) {
    if (-10 < x && x < 10) return x; // trivial case

    size_tlli sign = (x < 0) ? -1 : 1;
    char* s = positivei_to_a(x*sign); // int as string
    size_tlli l = strlen(s); // length of string

    // swap
    l--;
    char temp;
    for (size_tlli i = 0; i <= (l/2); i++) {
        temp = s[l-i];
        s[l-i] = s[i];
        s[i] = temp;
    }
    size_tlli answer = atoll(s);
    if (answer > 2147483647 || answer < -2147483648) return 0; // outside of range
    
    free(s);

    return sign * answer;
}