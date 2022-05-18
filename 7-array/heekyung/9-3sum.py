class Solution:
    '''
    배열을 입력받아 함을 3으로 만들 수 있는 3개의 엘리먼트 출력
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    '''
    def threeSum_bruteforce(self, nums:List[int]) -> List[List[int]]:
        # Time limit error o(n^3)
        result = []
        nums.sort() # 정렬

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(k+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i] , nums[j] , nums[k]])
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Runtime 1665 ms O(n^2)
        Memory 18 MB
        '''
        result = []
        nums.sort() # 정렬

        for i in range(len(nums)-2): # 첫번째 인덱스

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1 # 두번째 인덱스
            r = len(nums) -1 # 세번째 인덱스

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < 0: # 합이 0보다 작으면 두번째 인덱스 이동
                    l +=1
                elif three_sum > 0: # 합이 0보다 크면 세번째 인덱스 이동
                    r -= 1
                else: # 합이 같으면
                    result.append([nums[i], nums[l] , nums[r]])

                    while l<r and nums[l] == nums[l+1] : # 중복되는 값을 때까지 두번째 인덱스 이동
                        l +=1
                    l+=1

                    while l<r and nums[r] == nums[r-1]: # 중복되는 값을 때까지 세번째 인덱스 이동
                        r -=1
                    r-=1

        return result