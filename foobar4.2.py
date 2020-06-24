'''
Find the most possible bunnies to save in the time limit given the traversal time matrix
'''

def solution(times, times_limit):
    # Your code here
    minDist = minDists(times)
    for index, val in enumerate(minDist):
        if val[index] < 0:
            return [val for val in range(len(times) - 2)]
    possible = returnAll(len(times))
    for array in possible:
        if sum(minDist[array[index]][array[index + 1]] for index in range(len(array) - 1)) <= times_limit:
            final = [val - 1 for val in array[1:-1]]
            final.sort()
            return final
    return []

def returnAll(length):
    possible = []
    for number in range(length - 2, 0, -1):
        for bunny in range(1, length - 1):
            current = [bunny]
            create(length, number, possible, current)
    return possible

def create(length, number, possible, current):
    if len(current) == number:
        possible.append([0] + current + [length - 1])
    else:
        for bunny in range(1, length - 1):
            if bunny not in current:
                create(length, number, possible, current + [bunny])

def minDists(times):
    #implemented using Floyd-Warshall algorithm
    length = len(times)
    minDist=[[0] * length for index in range(length)]
    for index in range(length):
        for index2 in range(length):
            minDist[index][index2] = times[index][index2]
    for index in range(length):
        for index2 in range(length):
            for index3 in range(length):
                if minDist[index][index3] + minDist[index3][index2] < minDist[index][index2]:
                        minDist[index][index2] = minDist[index][index3] + minDist[index3][index2]
    return minDist
