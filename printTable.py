tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    # Size of tableData which is 4
    num_cols = len(tableData[0])

    # Longest strings in each of the inner lists
    col_widths = [max([len(item) for item in data]) for data in tableData]

    for row in range(num_cols):
        line = ""
        for col, data in enumerate(tableData):
            line += data[row].rjust(col_widths[col]) + " "
        print(line)

printTable(tableData)