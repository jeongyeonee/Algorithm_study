class Solution:
    '''
    n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 값을 구하여라
    '''

    def arrayPairSum(self, nums: List[int]) -> int:
        '''
        Time O(n)(297 ms)
        memory O(1)
        '''
        nums.sort()

        result = 0
        for i in range(0, len(nums), 2):
            #정렬된 리스트를 두 스텝씩 뛰어 더하면 페어 중 항상 작은값을 더 할 수 있다
            result+=nums[i]
        return result

    def arrayPairSum(self, nums: List[int]) -> int:
        # 파이썬 한문장으로 해결하기
        return sum(sorted(nums)[::2])