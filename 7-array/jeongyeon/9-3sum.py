'''
정연코드
Time Limit Exceeded
'''


def threeSum_fail(nums):
    if len(nums) < 3:
        return []
    result = []

    for i, n1 in enumerate(nums[:-2]):
        for j, n2 in enumerate(nums[i + 1:-1]):
            if (-n1 - n2) in nums[i + j + 2:]:
                tmp = sorted([n1, n2, (-n1 - n2)])
                if tmp in result:
                    continue
                result.append(tmp)
                print(n1, n2)
    return result


'''
투포인터 방식

정렬되어 있으면 투포인터 쓰기 좋음. (7-two-sum 문제 참고 p.176)
nums = [-2,0,0,2,2]의 경우, 동일한 값이 배열에 포함될 수 있으니
스킵처리 해줄 수 있도록 신경써야 함.

838 ms
'''


def threeSum_use_twopointer(nums):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            tmp = nums[i] + nums[left] + nums[right]
            if tmp < 0:
                left += 1
            elif tmp > 0:
                right -= 1
            else:
                print(i, left, right)
                result.append([nums[i], nums[left], nums[right]])
                # 진행해야 하는 다음방향과 값이 같으면, 스킵
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result
