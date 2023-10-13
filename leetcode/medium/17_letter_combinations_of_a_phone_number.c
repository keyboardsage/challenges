void generateWordCombos(char** generatedList, int generatedListSize, char** words, int wordsSize, char* buffer, int* activeDestination, int activeWord, int fillIndex) {
    // on the last character (leaf letter), copy the buffer
    if (activeWord == wordsSize) {
        //DEBUG: printf("==> %s \n", buffer);
        strncpy(generatedList[*activeDestination], buffer, wordsSize);
        (*activeDestination)++;
        return;
    }

    // for every letter in the current word...
    for (int c = 0; c < strlen(words[activeWord]); c++) {
        //DEBUG: printf("%d:%c ", c, words[activeWord][c]);

        buffer[fillIndex] = words[activeWord][c]; // ...set the character...

        generateWordCombos(generatedList, generatedListSize, 
            words, wordsSize, 
            buffer, activeDestination, 
            activeWord + 1, 
            fillIndex + 1);
    }
    //DEBUG: printf("\n");

    return;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** letterCombinations(char * digits, int* returnSize){
    // trivial case, null string
    if (digits[0] == '\0') {
        *returnSize = 0;
        return NULL;
    }

    // constants
    char* LETTERS[] = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    int LETTERS_LENGTH[] = {0,0,3,3,3,3,3,4,3,4};
    const int ASCII_NUMERIC_START = 48;

    // determine the number of c-strings to return
    *returnSize = 1;
    int digitAsInt = 0;
    for (int i = 0; digits[i] != '\0'; i++) {
        digitAsInt = digits[i] - ASCII_NUMERIC_START;
        (*returnSize) *= LETTERS_LENGTH[digitAsInt];
    }

    // allocate space for the final strings to be returned
    char** combinations = (char**)malloc((*returnSize) * sizeof(char*)); // list/rows
    for (int i = 0; i < (*returnSize); i++) { // c-string/columns
        combinations[i] = (char*)malloc((strlen(digits)+1) * sizeof(char));
        combinations[i][strlen(digits)] = '\0'; // terminate the strings up front
    }

    // for...
    char* words[strlen(digits)];
    //int digitAsInt = 0;
    for (int d = 0; d < strlen(digits); d++) { // ...each digit that was pressed...
        digitAsInt = digits[d] - ASCII_NUMERIC_START;
        words[d] = LETTERS[digitAsInt]; // ...add the associated string to the word list
    }

    // generate the word combos based on the word list and populate the combinations list
    char buffer[strlen(digits)+1];
    buffer[strlen(digits)] = '\0';
    int destination = 0;
    generateWordCombos(combinations, *returnSize, words, strlen(digits), buffer, &destination, 0, 0);
    
    return combinations;
}