'''
Finding the number of lucky triples - subsets of three numbers where each divides the next - in a list of integers
'''

def solution(l):
    total = 0
    first = [0] * len(l)
    second = [0] * len(l)
    for index, val in enumerate(l):
        for index2, val2 in enumerate(l[index+1:]):
            if val2 % val == 0:
                first[index] += 1
                second[index2 + index + 1] += 1
    for index, val in enumerate(first):
        total += val * second[index]
    return total