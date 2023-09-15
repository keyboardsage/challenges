int get_nth_digit(int number, int nth) {
    for (int n = nth; n != 0 ; n--) number /= 10;
    return number % 10;
}

bool isPalindrome(int x){
  if (x >= 0 && x < 10) return true;
  else if (x > 0)
  {
    // determine the number of digits in the number
    const int HIGHEST_POSSIBLE_POWER = 9;
    int digits_in_number = 0;
    for (int p = HIGHEST_POSSIBLE_POWER; p >= 0; p--)
        if ((x / (int)pow(10, p)) != 0) {
            digits_in_number = p+1;
            break;
        }
    
    // read both sides (i is on right, j is on left) and compare each place, short circuit false if digits mismatch
    for (int i = 0, j = digits_in_number-1; i < digits_in_number/2; i++, j--)
        if (get_nth_digit(x, i) != get_nth_digit(x, j)) return false;

    return true;
  }

  return false;
}