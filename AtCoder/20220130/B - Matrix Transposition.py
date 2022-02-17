h, w = list(map(int, input().split()))
matrixA = []
for i in range(h):
     matrixA.append(input().split())
matrixB = []
for j in range(w):
    temp = []
    for k in range(h):
        temp.append(matrixA[k][j])
    matrixB.append(temp)
for i in range(w):
    print(" ".join(matrixB[i]))