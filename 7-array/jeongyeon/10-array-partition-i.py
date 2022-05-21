
'''
정연풀이
377 ms

sort()를 이용했으나,
sorted 이용하여 한 줄 제거했어도 깔끔했을 것 같음.
'''
def arrayPairSum(nums):
    nums.sort()
    return sum(nums[::2])
