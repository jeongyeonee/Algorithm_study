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
