'''
정연코드

제약사항: 나눗셈을 하지 않고 O(n)에 풀이하라.

O(n) 풀이 실패
Time Limit Exceeded
'''
def productExceptSelf_fail(nums):
    def multiple(arr):
        mul = 1
        for a in arr:
            mul *= a
        return mul
    
    result = []
    while len(result) < len(nums):
        result.append(multiple(nums[1:]))
        nums.append(nums.pop(0))
    return result

'''
왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
315 ms
'''

def productExceptSelf(nums):
    result = []
    p = 1
    for i in range(len(nums)):
        result.append(p)
        p *= nums[i]
        
    p = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] = result[i]*p
        p *= nums[i]
    return result
   
