def solution(A, F, M):
    # Implement your solution here
    curTime = len(A)
    curSum = sum(A)

    total = (curTime+F) * M

    res = []

    for i in range(F):
        if total - curSum >= 6:
            res.append(6)
            curSum += 6
            continue
        for j in range(6,0,-1):
            if curSum + j == total:
                res.append(j)
                break 

    print(res)
    return res 

solution([1, 5, 6], 4, 3)