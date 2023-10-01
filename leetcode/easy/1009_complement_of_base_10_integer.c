int bitwiseComplement(int n){
    const int RADIX = 2;

    // build a mask where ones are in the indices necessary to represent `n` in binary
    unsigned int mask = 0;
    for (int i = 0; pow(RADIX, i) < n; i++) mask |= 1 << i;

    return ~n & mask; // inverse the integer and return the unsigned portion
}