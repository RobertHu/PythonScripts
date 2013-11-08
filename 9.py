matrix=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]
transposed = []
for i in range(4):
    transposed_row = []     
    for row in matrix:
        transposed_row.append(row[i])
        print(transposed_row)
    transposed.append(transposed_row)


