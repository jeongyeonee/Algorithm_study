class Solution:
    '''
    가장 긴 팰린트롬 부분을 분자열을 출력
    Input: s = "babad"
    Output: "bab"
    '''

    def longestPalindrome(self, s: str) -> str:
        '''
        문자열의 팰린드롬의 길이가 짝수일 경우와 홀수일 경우를 고려하여
        투 포인터를 설정하고 범위를 확장해가면서 팰린드롬인 경우를 구한다.
        '''

        def expand(l,r):

            # 법위에 벗어나지 않고 팰린드롬일 동안 포인터 확장
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        # 문자 길이가 1개거나 문자 전체가 PALINDROME일때
        if len(s) < 2 or s==s[::-1]:
            return s

        result = ''
        for i in range(len(s)-1):
            # PALINDROME 문자길이가 짝수일 경우 (i+1), 홀수일 경우(i+2) 확인
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)
        return result