'''
Finding the largest number that can be made from a list of digits that is divisible by 3
'''

def solution(l):
    # Your code here
    threeDiv, numbers = [], []
    l = sorted(l)
    l.reverse()
    findCombos(threeDiv, l)
    if (len(threeDiv)):
        for sub in threeDiv:
            number = 0
            for val in sub:
                number = number * 10 + val
            numbers.append(number)
        return str(max(numbers))
    return('0')
    
def findCombos(threeDiv, l):
    if len(l):
        if sum(l) % 3 == 0 and l not in threeDiv:
            threeDiv.append(l)
        for index, _ in enumerate(l):
            findCombos(threeDiv, l[:index] + l[index + 1:])