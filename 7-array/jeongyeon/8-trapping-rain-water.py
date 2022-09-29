'''
투포인터 사용
143 ms

가장 높은 곳에서 두 포인터가 만나면 끝
(두 포인터 비교해서 높은쪽으로 한 칸 전진)

각 포인터가 여태까지 지나왔던 높이 중 max에서 현재 높이를 빼서 volume에 더함.
'''
def trap_use_twopointer(height):
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max , right_max = max(left_max, height[left]),\
                                max(right_max, height[right])
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
