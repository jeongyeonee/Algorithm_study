class Solution:
    '''
    product of array except self
    배열을 입력 받아 output[i] 자신을 제외한 나머지 요소들의 곱을 output[i]에 저장하라

    '''
    class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            '''
            Time O(n) 300 ms
            Memory O(1)
            '''
            # 리턴할 리스트
            result = [0] * len(nums)

            # result[i]는 왼쪽에 있는 element들을 곱한 값을 저장한다
            # 첫번째 인덱스는 왼쪽의 값이 없기 때문에 1을 저장
            result[0] = 1
            for i in range(1, len(nums)):
                # result[i-1]는 이미 i-1까지 누적된 곱을 가짐
                result[i] = nums[i-1] * result[i-1]

                # 반대로 오른쪽의 있는 값들을 곱해준다
            # 맨 마지막 인덱스는 오른쪽의 값이 없기 때문에 1을 저장하여 곱해줌
            r = 1
            for i in reversed(range(len(nums))):
                # r의 값을 nums[i]와 곱하여 갱신함으로써 result[i]에 누적된 곲을 저장함
                result[i] = result[i] * r
                r *= nums[i]

            return result