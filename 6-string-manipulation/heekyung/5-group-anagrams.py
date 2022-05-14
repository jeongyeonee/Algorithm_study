class Solution:
    '''
    문자열을 받아 애너그램 단위로 그룹핑하기
    '''
    def groupAnagrams(self, strs: List[str])-> List[List[str]]:
        '''
        collections.defaultdict(list)을 활용하여
        단어를 정렬했을때 동일한 경우를 하나의 리스트로 묶는다
        '''
        import collections
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())
