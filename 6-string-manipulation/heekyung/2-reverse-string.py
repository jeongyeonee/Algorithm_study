class Solution:
    '''
    문자열 뒤집기
    리턴 없이 O(1) 메모리로 해겷해야함
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    '''
    def reverseString_python(self, s: List[str]) -> None:
        '''
        파이썬 함수로 풀기
        '''
        s.reverse()

        # .reverse()는 반환 하지 않으며 리스트 자체를 변환 시킨다
        # 혹은 s[:] = s[::-1] 사용가능

    def reverseString(self, s: List[str]) -> None:
        '''
        투포인터로 풀기
        '''
        l, r = 0, len(s) -1
        while l < r:
            # s 내부 스왑
            s[l], s[r] = s[r], s[l]
            # 포인터 이동
            l += 1
            r -= 1


