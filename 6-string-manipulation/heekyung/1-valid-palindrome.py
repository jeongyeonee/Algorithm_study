class Solution:
    '''
    주어진 문자열이 팰린드롬인지 확인하는 문제
    대소문자 구분하지 않으며, 영문자와 숫자많을 대상으로 한다.

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    '''
    def isPalindrome_list(self, s: str) -> bool:
        '''
        리스트로 변환 하기
        리스트 보다 데크를 사용하는 것이 더 빠르다
        '''
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        #팰린드롬 판별 여부
        while len(strs) > 1:
            if s.pop(0) != s.pop():
                return False
        return True

    def isPalindrome_deque(self, s: str) -> bool:
        '''
        데크를 명시적으로 사용하는 것이 더 빠르다
        '''
        import collections

        strs = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        #팰린드롬 판별 여부
        while len(strs) > 1:
            if s.popleft() != s.pop():
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        '''
        파이썬의 슬라이싱과 정규표현식으로 가장빠르게 구현 가능
        '''
        import re

        # filter unecessary char
        #[] :[]안에 들어있는 캐릭터 자체를 나타내며
        # ^ : 맨 앞에 사용될 경우에만 해당 문자 패턴이 아닌 것과 매칭 ex) [^a-d] : a 그리고 b 그리고 c 그리고 d 가 아닌 문자열
        # - : 해당 문자 사이 범위에 속하는 문자 중 하나 ex) [a-d] : a 또는 b 또는 c 또는 d
        s = s.lower()
        s = re.sub('[^0-9a-z]','',s)

        return  s == s[::-1] #문자열 뒤집기
