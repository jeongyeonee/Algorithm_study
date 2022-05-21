'''
브루트포스 방법은 가장 비효율적인 방법
3337 ms
'''

def twoSum_bruteforce(nums, target):
    for i, n in enumerate(nums[:-1]):
        for j, m in enumerate(nums[i+1:]):
            if n+m == target:
                print(i, n, j, m)
                return [i, j+i+1]

'''
in 이용
676 ms
'''
def twoSum_use_in(nums, target):
    for i, n in enumerate(nums[:-1]):
        if target - n in nums[i+1:]:
            return [i, nums[i+1:].index(target-n)+i+1]

'''
dictionary를 이용하여 찾기
1049 ms
'''
def twoSum_use_dict(nums, target):
    nums_dict = {}
    for i, n in enumerate(nums):
        nums_dict[n] = i
    for i, n in enumerate(nums):
        if (target - n in nums) and (i != nums_dict[target-n]):
            return [i, nums_dict[target-n]]


'''
dictionary 이용하여 찾기2
하나의 for 문을 이용
77ms
'''
def twoSum_use_dict2(nums, target):
    nums_dict = {}
    for i, n in enumerate(nums):
        if target-n in nums_dict:
            return [nums_dict[target-n], i]
        nums_dict[n] = i


'''
투포인터 이용
nums 배열은 정렬되어 있지 않음.
인덱스를 찾아야 하는 문제이기 때문에 투포인터 사용 불가.
값을 찾아야 하는 문제라면 사용 가능 했을 것임
'''
def twoSum_use_twopointer(nums, target):

    left, right = 0, len(nums)-1
    while left != right:
        print(left, right)
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
