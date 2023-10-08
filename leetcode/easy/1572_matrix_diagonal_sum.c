int diagonalSum(int** mat, int matSize, int* matColSize){
    int primary = 0;
    int secondary = 0;
    for (int i = 0; i < matSize; i++)
        for (int j = 0; j < *matColSize; j++)
            if (i == j)
                if (*matColSize - j - 1 == j) primary += mat[i][j];
                else {
                    primary += mat[i][j];
                    secondary += mat[i][*matColSize - j - 1];
                }

    return primary + secondary;
}