int sumBase(int n, int k){
    size_t remainder = 0;
    size_t accumulator = 0;

    for (int i = 0; n != 0; i++) {
        // calculate the number in radix k
        remainder = n % k;
        n = n / k;

        // set up a base 10 integer
        accumulator += remainder;
    }

    return accumulator;
}