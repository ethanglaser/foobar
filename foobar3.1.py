'''
Finding the distribution of ratios across the different terminal states using Markov limiting matricies
'''

def solution(m):
    # Your code here
    #please excuse how unpolished the code is, sorrey
    #thanks to stackPusher for a little help with inverting (https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy) and patrickJMT for a little help understanding Markov Matrices (https://www.youtube.com/watch?v=BsOkOaB8SFk)
    terminals, final = [],[]

    for index, val in enumerate(m):
        if sum(val) == 0:
            terminals.append(index)

    if sum(m[0]) == 0:
        final = [1] + [0] * (len(terminals) - 1) + [1]
        return final
    
    if len(terminals) + 1 >= len(m):
        final = simplify(m[0][1:] + [sum(m[0][1:])])
        return final

    n = [[0 for i in range(len(m))] for j in range(len(m))]
    key, R, Q, QQ, ret = [], [], [], [], []

    n = rearrange(m, terminals, key, n)
    for row in n[len(terminals):]:
        R.append(row[:len(terminals)])
        Q.append(row[len(terminals):])

    for index, row in enumerate(Q):
        newRow = []
        for index2, val in enumerate(row):
            if index == index2:
                newRow.append([val[1] - val[0], val[1]])
            else:
                newRow.append([0 - val[0], val[1]])
        QQ.append(newRow)
    F = invert(QQ)
    final = matrixMultiply(F,R)[key.index(0) - len(terminals)]
    lcm = final[0][1]
    for val in final:
        lcm = lcmFind(lcm, val[1])
    for val in final:
        ret.append(int(val[0] * lcm / val[1]))
    for index, val in enumerate(ret):
        if val == sum(ret) and val != 1:
            ret[index] = 1
    ret.append(sum(ret))
    ret = simplify(ret)
    return ret

def matrixMultiply(m1, m2):
    product = [[[0,0] for i in range(len(m2[0]))] for j in range(len(m1))]
    for index, row in enumerate(product):
        for index2, val in enumerate(row):
            for index3, val2 in enumerate(m1[0]):
                product[index][index2] = simplify(addFraction(product[index][index2], fractionMultiply(m1[index][index3], m2[index3][index2])))
    return product

def transpose(m):
    n = [[[0,0] for i in range(len(m[0]))] for j in range(len(m))]
    for index, row in enumerate(m):
        for index2, val in enumerate(row):
            n[index2][index] = val
    return n

def getMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]    

def getDeterminant(m):
    if len(m) == 2:
        return fractionSubtract(fractionMultiply(m[0][0],m[1][1]), fractionMultiply(m[0][1],m[1][0]))
    determinant = [0,0]
    for c in range(len(m)):
        if c % 2:
            cc = 1
        else:
            cc = -1
        a = fractionMultiply([cc,1],m[0][c])
        b = getDeterminant(getMinor(m,0,c))
        determinant = simplify(addFraction(determinant,fractionMultiply(a,b)))
    return determinant

def fractionDivide(arg1, arg2):
    return(simplify([arg1[0] * arg2[1], arg1[1] * arg2[0]]))

def invert(m):
    det = getDeterminant(m)
    if len(m) == 2:
        return [[fractionDivide(m[1][1],det), fractionMultiply([-1,1],fractionDivide(m[0][1],det))],[fractionMultiply([-1,1],fractionDivide(m[1][0],det)), fractionDivide(m[0][0],det)]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMinor(m,r,c)
            if (r + c) % 2:
                cc = 1
            else:
                cc = -1
            a = simplify(fractionMultiply([cc,1], getDeterminant(minor)))
            cofactorRow.append(a)
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = fractionDivide(cofactors[r][c],det)
    return cofactors

def rearrange(original, terminals, key, new):
    key2 = []
    for index, _ in enumerate(original):
        if index in terminals:
            key.append(index)
        else:
            key2.append(index)
    key += key2
    for index, val in enumerate(original):
        for index2, _ in enumerate(val):
            new[index][index2] = original[key[index]][key[index2]]
    for index, row in enumerate(new):
        if sum(row) == 0:
            new[index][index] = 1
    new = fractionMatrix(new)
    return new

def lcmFind(arg1, arg2):
    index = 1
    while index < arg1 * arg2:
        if index % arg1 == 0 and index % arg2 == 0:
            return index
        index += 1
    return arg1 * arg2

def fractionMatrix(m):
    n = []
    for index, row in enumerate(m):
        row[index] = 0
        newRow = []
        for val in row:
                newRow.append([val, sum(row)])
        n.append(newRow)
    return n

def simplify(arg1):
    status = True
    for val in arg1:
        if val > 0:
            status = False
    if status:
        for index,val in enumerate(arg1):
            arg1[index] = -val
    if arg1[0] < 0 and arg1[1] < 0:
        arg1[0] *= -1
        arg1[1] *= -1
    num = 2
    if arg1[0] == 0 and len(arg1) == 2:
        return [0, 1]
    while num <= max(arg1):
        status = True
        for val in arg1:
            if val % num != 0:
                status = False
        if status:
            for index, val in enumerate(arg1):
                arg1[index] = int(val / num)
        else:
            num += 1
    return arg1

def addFraction(arg1, arg2):
    if arg1 == [0, 0]:
        return arg2
    elif arg2 == [0, 0]:
        return arg1
    else:
        return [arg1[0] * arg2[1] + arg1[1] * arg2[0], arg1[1] * arg2[1]]

def fractionMultiply(arg1, arg2):
    return(simplify([arg1[0] * arg2[0], arg1[1] * arg2[1]]))

def fractionSubtract(arg1, arg2):
    if arg1 == [0, 0]:
        return [-arg2[0], arg2[1]]
    elif arg2 == [0, 0]:
        return arg1
    else:
        return [arg1[0] * arg2[1] - arg1[1] * arg2[0], arg1[1] * arg2[1]]
