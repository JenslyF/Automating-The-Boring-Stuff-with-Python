# Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# defines function 
def printGrid(gridTable):
  
  rows = len(gridTable) # Number of rows (9)
  cols = len(gridTable[0]) # Number of columns (6)
  
  # we want to print all the column values from row 1, row 2, etc
  for j in range(cols): # Traverses columns
    for i in range(rows): # Traverses rows
        print (gridTable[i][j], end=" ") # Prints the nested values and doesn't add a line after each of them
    print()  # Adds newline at the end of each list
               # or print(' ') also works
      
     
# Calls function and makes it execute       
printGrid(grid)
      