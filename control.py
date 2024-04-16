# matrix = []

# for i in range(0, 8):
#     tmp = []
#     for j in range(0, 11):
#         tmp.append(0)
    
#     matrix.append(tmp)
    

# for w in range (1, 7*8):
#     i, j, d = input().split()
#     matrix[int(i)][int(j)] = int(d)
    
# for i in range(0, 8):
#     for j in range(0, 11):
#         print(matrix[i][j], end = ", ")
#     print("")
    

# 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
# 0, 1, 0, 5, 0, 2, 1, 0, 5, 0, 2,
# 0, 8, 0, 9, 5, 7, 7, 5, 9, 0, 6,
# 0, 3, 0, 6, 3, 2, 1, 4, 8, 0, 4,
# 0, 1, 0, 9, 0, 2, 1, 0, 9, 0, 2,
# 0, 3, 2, 8, 5, 7, 7, 5, 6, 1, 4,
# 0, 1, 7, 4, 3, 2, 1, 4, 3, 7, 2,
# 0, 3, 0, 0, 0, 7, 7, 0, 0, 0, 4,

px_X = []

for i in range(0, 547):
    px_X.append(-1)

px_X[1] = 1
px_X[39] = 2
px_X[99] = 3
px_X[159] = 4
px_X[217] = 5
px_X[277] = 6
px_X[337] = 7
px_X[397] = 8
px_X[456] = 9
px_X[496] = 10

px_Y = []

for i in range(0, 547):
    px_Y.append(-1)

px_Y[1] = 1
px_Y[71] = 2
px_Y[124] = 3
px_Y[336] = 4
px_Y[389] = 5
px_Y[442] = 6
px_Y[495] = 7