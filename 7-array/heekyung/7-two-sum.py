class Solution:
    '''
    덧셈하여 타겟을 만들 수ㅜ 있는 두배열의 두숫자 인덱스를 리턴
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    '''
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        '''
        브루트 포스로 계산
        Runtime: 4500 ms
        Memory: 14.9 MB
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if target == nums[i]+nums[j]:
                    return [i, j]

    def twoSum_usingIn(self, nums: List[int], target: int) -> List[int]:
        '''
        포문을 돌면서 필요한 남은 값을 파악하고 남는 값이 남은 리스트에 있다면 반환
        Runtime: 916 ms
        Memory: 14.9 MB
        '''
        for i in range(len(nums)):

            # 타겟에서 현재 값 빼서 필요한 값 파악
            complement = target - nums[i]

            # 남은 리스트에서 필요한 값 존재하면 반환
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i+1)]

    def twoSum_usingDict(self, nums: List[int], target: int) -> List[int]:
        '''
        시간복잡도를 개선하기 위해 딕셔너리에 숫자리스트를 저장하고
        포문마다 돌면서 첫번째 수를 뺀 결과 키를 조회하기
        Runtime: 136 ms
        Memory: 15.4 MB
        '''
        # 키를 num 값을 index로 딕셔너리 저장
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return i, nums_map[target-num]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        위의 twoSum_usingDict을 개선하여 하나의 포문으로 처리
        Runtime: 136 ms
        Memory: 15.4 MB
        '''
        # 키를 num 값을 index로 딕셔너리 저장
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return i, nums_map[target-num]
            nums_map[num] = i