'''
정연풀이
현재 값과 max(다음 값부터 전체)를 비교

Time Limit Exceeded
'''

def maxProfit_fail(prices):
    result = 0
    for i, n in enumerate(prices[:-1]):
        tmp = max(prices[i+1:]) - n
        if tmp > result:
            result = tmp
    return result



'''
저점과 현재 값과의 차이 계산

1458 ms

'''
def maxProfit(prices):
    import sys
    min_price = sys.maxsize
    profit = 0

    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)
    return profit
