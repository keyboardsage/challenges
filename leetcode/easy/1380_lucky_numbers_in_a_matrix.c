int matrix_minimum_in_row(int** matrix, int row, int columnSize) {
    int minimumColumnIndex = 0; // begin by assuming first column in row is the minimum

    for (int j = 0; j < columnSize; j++)
        if (matrix[row][minimumColumnIndex] > matrix[row][j])
            minimumColumnIndex = j;
    
    return minimumColumnIndex; // return index of the minimum value on the row
}

int matrix_maximum_in_column(int** matrix, int rowSize, int column) {
    int maximumRowIndex = 0; // begin by assuming first row in column is the maximum

    for (int i = 0; i < rowSize; i++)
        if (matrix[maximumRowIndex][column] < matrix[i][column])
            maximumRowIndex = i;
    
    return maximumRowIndex;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* luckyNumbers (int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    int* returnValue = (int*)malloc(matrixSize * sizeof(int));
    int returnValueIndex = 0;

    // for each row...
    int columnIndex = 0;
    int rowIndex = 0;
    for (int row = 0; row < matrixSize; row++) {
        // find the minimum value on the row and return it's column index...
        columnIndex = matrix_minimum_in_row(matrix, row, *matrixColSize);

        // find the maximum value on the column and return it's row index...
        rowIndex = matrix_maximum_in_column(matrix, matrixSize, columnIndex);

        // ...remember the solutions
        if (row == rowIndex) {
            returnValue[returnValueIndex] = matrix[rowIndex][columnIndex];
            returnValueIndex++;
        }
    }
    
    *returnSize = returnValueIndex;
    return returnValue;
}