def longestPalindrome(s):

    '''
    2칸, 3칸으로 구성된 투 포인터가 슬라이딩 윈도우처럼 전진
    이 때 윈도우에 들어온 문자열이 팰린드롬이면 포인터 확장
    '''
    def check(left, right):
        while left >= 0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) <= 1 or s==s[::-1]:
        return s

    result = ''
    for i in range(len(s)-1):
        result = max(result,
                     check(i, i+1),
                     check(i, i+2),
                     key = len)
    return result
