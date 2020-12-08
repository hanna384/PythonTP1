def multiplication(mat1, mat2):
    for c in range(3):
        for l in range(3):
            for i in range(3):
                mat3[c][l] +=  mat1[i][l] * mat2[c][i]
            return (mat3[c][l])