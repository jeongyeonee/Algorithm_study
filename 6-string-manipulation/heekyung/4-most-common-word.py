class Solution:
    '''
    금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
    대소문자 구분하지 않으며, 구두점(.,) 무시

    Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
    Output: "ball"
    '''
    def mostCommonWord_(self, paragraph: str, banned: List[str]) -> str:
        '''
        collections.defaultdict(int)을 사용하여 문자열의 개수를 구하고 반환하는 방법
        '''
        import re
        import collections
        # Preprocess string
        # ^ : not
        # \w: word character
        # replace non-word character to ''
        # make all lower case
        paragraph = re.sub('[^\w]', ' ', paragraph).lower()
        #paragraph = re.sub('[!?'',;.]', '', paragraph).lower()

        words = paragraph.split()
        words = [word for word in words if word not in banned]

        # count word with defalut dict 0
        counts = collections.defaultdict(int)
        for word in words:
           counts[word] += 1

        return max(counts, key=counts.get)

    def mostCommonWord_(self, paragraph: str, banned: List[str]) -> str:
        '''
        collections.Counter를 사용하여 코드를 더 간소화
        '''
        import re
        import collections
        # Preprocess string
        # ^ : not
        # \w: word character
        # replace non-word character to ''
        # make all lower case
        paragraph = re.sub('[^\w]', ' ', paragraph).lower()
        # paragraph = re.sub('[!?'',;.]', '', paragraph).lower()

        words = paragraph.split()
        words = [word for word in words if word not in banned]

        # 가장 첫번째로 많이 나오는 값
        count = collections.Counter(words)
        most_common = count.most_common(1)

        return most_common[0][0]
