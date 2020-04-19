'''
Finding the indexes of the beginning and end of the first subset of numbers in a list that add to the desired value
'''

def solution(l, t):
    # Your code here
    for index, _ in enumerate(l):
        for index2 in range(index, len(l)):
            if sum(l[index:index2 + 1]) == t:
                return [index, index2]
    return [-1, -1]