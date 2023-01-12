# LRU 알고리즘
# Cache Hit : CPU 가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우 1
# Cache Miss : CPU 가 참조하고자 하는 메모리가 캐시에 존재하지 않을 경우 5
def solution(cacheSize, cities):
    from collections import deque
    if cacheSize == 0:
        return 5 * len(cities)

    answer = 0
    cities = [c.lower() for c in cities]
    cache = deque()

    idx = 0
    while len(cache) < cacheSize:
        c = cities[idx]
        if c in cache:
            cache.remove(c)
            answer+= 1
        else:
            answer += 5
        cache.appendleft(c)
        idx += 1

    for c in cities[idx:]:
        if c in cache:
            answer += 1
            cache.remove(c)
        else:
            answer += 5
            cache.pop()
        cache.appendleft(c)

    return answer

# 위 함수보다 간결
def solution2(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    answer = 0
    cities = [c.lower() for c in cities]
    cache = []

    for c in cities:
        if c in cache:
            cache.remove(c)
            answer += 1
        else:
            if cacheSize == len(cache):
                cache.pop(0)
            answer += 5
        cache.append(c)

    return answer
