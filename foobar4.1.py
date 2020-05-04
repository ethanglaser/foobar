'''
Find the fewest possible unpaired guards given a list of the number of bananas each has
'''

def solution(banana_list):
    #Your code here
    #first created a list of dicts to represent the guards with the number of bananas and a list of guards they are compatible with
    graphDict = []
    for index, val in enumerate(banana_list):
        graphDict.append({})
        graphDict[index]['value'] = val
        graphDict[index]['edges'] = []
    for index1, val in enumerate(graphDict):
        for index2, guard in enumerate(graphDict[index1 + 1:]):
            if not isBad(val['value'], guard['value']):
                val['edges'].append(index2 + index1 + 1)
                guard['edges'].append(index1)
    return makePairs(graphDict)

#optimally pairs up guards until not possible, returns the number of unpaired guards
def makePairs(graphDict):
    #original is the indexes of graphDict that are not yet paired but still have compatible possibilities
    original = [val for val in range(len(graphDict))]
    paired, unpaired = [], []
    while len(original):
        #first removes guards with no possible remaining pairings and adds them to the unpaired list
        for node in original:
            if len(graphDict[node]['edges']) == 0:
                unpaired.append(node)
        original = [element for element in original if element not in unpaired]
        if len(original):
            #next finds the guard with the fewest compatible guards and its compatible guard with the fewest compatible guards and pairs them
            minNode = original[0]
            minVal = len(graphDict[minNode]['edges'])
            for node in original:
                if minVal > len(graphDict[node]['edges']):
                    minNode = node
                    minVal = len(graphDict[node]['edges'])
            minConnect = graphDict[minNode]['edges'][0]
            minVal = len(graphDict[minConnect]['edges'])
            for connect in graphDict[minNode]['edges']:
                if minVal > len(graphDict[connect]['edges']):
                    minConnect = connect
                    minVal = len(graphDict[connect]['edges'])
            original.remove(minNode)
            original.remove(minConnect)
            for node in original:
                if minNode in graphDict[node]['edges']:
                    graphDict[node]['edges'].remove(minNode)
                if minConnect in graphDict[node]['edges']:
                    graphDict[node]['edges'].remove(minConnect)
            paired.append((graphDict[minNode]['value'], graphDict[minConnect]['value']))
    return len(unpaired)

#reduces 2 numbers to relatively prime
def simplify(val, val2):
    div = 2
    if val2 % val == 0:
        return 1, val2 / val
    if val % val2 == 0:
        return val / val2, 1
    while div ** 2 < (min([val, val2]) + 1):
        if range(val % div == 0 and val2 % div == 0):
            val /= div
            val2 /= div
        else:
            div += 1
    return val, val2

#determines if a pair of numbers will eventually become equal - numbers already equal and numbers of opposite even/odd are easy cases
def isBad(val1, val2):
    if val1 == val2:
        return True
    if val1 % 2 != val2 % 2:
        return False
    #for more complex pairs, I tinkered around and discovered that a pair of numbers will be bad if the reduced pair adds to a power of two
    simpleSum = sum(simplify(val1, val2))
    while simpleSum:
        if simpleSum == 1:
            return True
        elif simpleSum % 2 == 0:
            simpleSum /= 2
        else:
            return False    