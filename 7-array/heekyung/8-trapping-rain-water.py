class Solution:
    '''
    높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    '''

    def trap_twopointer(self, height: List[int]) -> int:
        '''
        투 포인터를 최대로 이동
        최대 높이의 막대까지 각각 좌우 포인터가 이동하며 그동안 좌우 기둥의 현재 최대 높이와 현재 높이의 차이만큼
        물 높이를 더해 나간다
        최대 지전에서 좌우 포인터가 만나면서 O(n)에 풀이가 가능하다.
        Runtime: 186 ms O(n)
        Memory: 15.7 MB
        '''
        # 리스트가 0이면 return 0
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            #더 높은 쪽으로 투포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

    def trap(self, height: List[int]) -> int:
        '''
        스택에 쌓아나가면서 현재 높이가 이전 높이보다 높을 때를 기준으로
        격차만큼 물 높이 최우기
        Runtime: 200 ms O(n)
        Memory: 15.7 MB
        '''
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우 = 스택의 마지막 값과 비교
            while stack and stack[-1] < height[i]:

                # 스택에서 꺼내기
                top = stack.pop()

                if not len(stack):
                    break
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]-height[top])

                volume += distance * waters
            stack.append(i)
        return volume