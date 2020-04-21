'''
Finding the minimum number of operations (add 1, subtract 1, divide by 2) it takes to reach 1
'''

def solution(n):
    # Your code here
    ops = recursive(int(n), 0)
    return ops

def recursive(n, ops):
    if n == 1:
        return ops
    if n % 2 == 0:
        return recursive(n / 2, ops + 1)
    elif n % 4 == 3 and n != 3:
        return recursive((n + 1) / 4, ops + 3)
    else:
        return recursive((n - 1) / 2, ops + 2)