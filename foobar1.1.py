'''
Finding a string of 5 integers in the sequence of primes given an index
'''

def solution(i):
    # Your code here
    currentLen = 0
    currentInt = 2
    finalLen = i + 5
    primeString = ""
    while currentLen < finalLen:
        if isPrime(currentInt):
            primeString += str(currentInt)
            currentLen += len(str(currentInt))
        currentInt += 1
    return primeString[i:i+5]
        
def isPrime(number):
    for n in range(2, number):
        if number % n == 0 and number != n:
            return False
    return True