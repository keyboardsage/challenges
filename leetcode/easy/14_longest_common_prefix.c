char * longestCommonPrefix(char ** strs, int strsSize){
    // memory for saving the longest common prefix
    const int MAX_WORD_LENGTH = 200;
    char* longest_prefix = (char*)malloc((MAX_WORD_LENGTH+1) * sizeof(char));
    memset(longest_prefix, '\0', (MAX_WORD_LENGTH+1) * sizeof(char));

    char* ref = strs[0]; // use first string as a reference
    
    if (strsSize == 1) return ref; // if its the trivial case, single element array, just return the first string

    // advance through each character...
    int j = 0;
    for (; j < MAX_WORD_LENGTH; j++) {
        // ...in all words one at a time
        for (int i = 0; i < strsSize; i++) {
            // if there is a printable character match, continue checking characters in remaining words
            if (ref[j] != '\0' && ref[j] == strs[i][j]) continue;

            // if there isn't a match, return the common prefix characters up until this point
            else goto RETURN_COMMON_PREFIX;
        }
    }

RETURN_COMMON_PREFIX:
    for (int k = 0; k < j; k++)
        longest_prefix[k] = ref[k];

    return longest_prefix; // will never get here, but it would return whatever is in longest_prefix
}