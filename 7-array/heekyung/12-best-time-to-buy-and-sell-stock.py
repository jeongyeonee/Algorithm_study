class Solution:
    '''
    한번의 거래로 최대의 이익을 낼 수 있는 이익을 반환
    '''
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time O(n) 1046 ms
        Memory O(1)
        '''
        min_price = sys.maxsize
        profit = 0

        for i in range(len(prices)):
            price = prices[i]

            if price < min_price:
                min_price = price

            profit = max(profit, price - min_price)

        return profit
