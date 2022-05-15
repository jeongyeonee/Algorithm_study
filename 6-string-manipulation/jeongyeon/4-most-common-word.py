class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter

        s_list = []
        paragraph = re.sub('[^a-z]', ' ', paragraph.lower())
        s_list = [p for p in paragraph.split() if p not in banned]

        s_list = sorted(Counter(s_list).items(), key=lambda x:-x[1])
        return s_list[0][0]

# 57 ms

'''
Counter 적용한 결과에 most_common() 함수 이용하면
sorted 하지 않아도 가장 많이 나온 단어 출력할 수 있음.
'''
