import random
import heapq


def pickMachine(machines, possible):
    pickMap = {1: 0, 2: 0, 3: 0, 4: 0}
    same = {1: 0, 2: 0, 3: 0, 4: 0}

    possible = [sum(possible[0:i+1]) for i in range(4)]


    for time in range(10000):
        pickeds = helper(possible)
        if len(pickeds) == 1:
            same[pickeds[0]+1] += 1
        else:
            for picked in pickeds:
                pickMap[picked + 1] += 1

    print(pickMap)
    minHeap = []
    for key in pickMap.keys():
        heapq.heappush(minHeap, (pickMap[key], key))


    return [heapq.heappop(minHeap)[1] for _ in range(2)]


def helper(possible):
    picked = []
    for i in range(2):
        pick = random.randint(0, 100)
        if 0 <= pick <= possible[0]:
            picked.append(0)
        elif possible[0] < pick <= possible[1]:
            picked.append(1)
        elif possible[1] < pick <= possible[2]:
            picked.append(2)
        elif possible[2] < pick <= possible[3]:
            picked.append(3)

    if set(picked) == 1:
        return picked[:1]
    else:
        return picked

machines = [1, 2, 3, 4]
possible = [20, 35, 25, 20]
pickMachine(machines, possible)