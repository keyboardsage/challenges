void reverseString(char* s, int sSize){
    for (int i = 0, j = sSize-1; i < sSize/2; i++, j--) {
        //printf("%d %d\n", i, j);

        // swaps safely provided that s[i] and s[j] aren't the same memory location
        s[i] ^= s[j];
        s[j] ^= s[i];
        s[i] ^= s[j];
    }
}