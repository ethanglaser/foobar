def solution(w, h, s):
    # Your code here
    if s == 1:
        return 1
    if w == 1:
        w = h
        h = 1
    if h == 1:
        start1 = 1
        start2 = 0
        final = 0
        while start1 <= s and start2 <= w - 1:
            final += choose(s, start1) * choose(w - 1, start2)
            start1 += 1
            start2 += 1
        return int(final)
        
def choose(val, val2):
    product = 1
    start = val
    while start > max(val2, val - val2):
        product *= start
        start -= 1
    div = min(val2, val - val2)
    while div:
        product /= div
        div -= 1
    return product



if __name__ == "__main__":
    print(solution(2,1,2))
