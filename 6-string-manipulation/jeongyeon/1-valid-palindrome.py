class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        
        s = s.lower()
        s_list = list(re.sub('[^a-zA-Z0-9]', '', s))
        
        if len(s_list)<=1:
            return True

        a = s_list[:len(s_list)//2]
        b = s_list[::-1]
        b = b[:len(s_list)//2]
        
        return a==b

# 55ms
