/* Generic reusable list code */
void list_populate_with_value(int* list, int length, int value) {
    for (int k = 0; k < length; k++)
        list[k] = value;
}

/* Island perimeter code */
int islandPerimeterHelper(int** grid, int gridSize, int* gridColSize, int row, int column, int* visited) {
    printf("(%d, %d):%d\n", row, column, grid[row][column]);

    // do not repeat cells
    if (visited[(row * (*gridColSize))+column] == 1) return 0;
    visited[(row * (*gridColSize))+column] = 1;

    // peek at adjacent cells to determine if there is perimeter to be added
    // note: inverse of these booleans indicate where there is more land, which will be useful later
    bool isInvalidOrLakeTileNorth = (row == 0)                     ? true : ((grid[row-1][column] == 0) ? true : false);
    bool isInvalidOrLakeTileSouth = (row == (gridSize-1))          ? true : ((grid[row+1][column] == 0) ? true : false);
    bool isInvalidOrLakeTileEast  = (column == ((*gridColSize)-1)) ? true : ((grid[row][column+1] == 0) ? true : false);
    bool isInvalidOrLakeTileWest  = (column == 0)                  ? true : ((grid[row][column-1] == 0) ? true : false);

    printf("(%d, %d):%d - %d, %d, %d, %d\n", row, column, grid[row][column], 
    isInvalidOrLakeTileNorth,
    isInvalidOrLakeTileWest,
    isInvalidOrLakeTileEast,
    isInvalidOrLakeTileSouth);

    // determine the perimeter number based on the number of adjacent water tiles
    return (isInvalidOrLakeTileNorth + isInvalidOrLakeTileWest + isInvalidOrLakeTileEast + isInvalidOrLakeTileSouth) +
        ((!isInvalidOrLakeTileNorth)  ? islandPerimeterHelper(grid, gridSize, gridColSize, row-1, column, visited) : 0) +
        ((!isInvalidOrLakeTileWest)   ? islandPerimeterHelper(grid, gridSize, gridColSize, row, column-1, visited) : 0) +
        ((!isInvalidOrLakeTileEast)   ? islandPerimeterHelper(grid, gridSize, gridColSize, row, column+1, visited) : 0) +
        ((!isInvalidOrLakeTileSouth)  ? islandPerimeterHelper(grid, gridSize, gridColSize, row+1, column, visited) : 0);
}

int islandPerimeter(int** grid, int gridSize, int* gridColSize){
    // find a land cell
    int i = 0;
    int j = 0;
    for (; i < gridSize; i++) {
        j = 0; // reset per row

        for (; j < *gridColSize; j++) // try to find land
            if (grid[i][j] == 1) goto CALCULATE_PERIMETER;
    }
    
    // return zero if there aren't any land cells
    if (gridSize == i && *gridColSize == j && grid[gridSize-1][(*gridColSize)-1] == 0) return 0;

    // calculate island's perimeter
CALCULATE_PERIMETER:
    int length = gridSize * (*gridColSize); // make list
    int* visited = (int*)malloc(length * sizeof(int));
    list_populate_with_value(visited, length, 0);

    printf("%d %d %d %d\n", gridSize, *gridColSize, i, j);
    if (i == gridSize) i--;
    if (j == *gridColSize) j--;
    int answer = islandPerimeterHelper(grid, gridSize, gridColSize, i, j, visited); // find answer

    free(visited); // clean up list

    return answer;
}