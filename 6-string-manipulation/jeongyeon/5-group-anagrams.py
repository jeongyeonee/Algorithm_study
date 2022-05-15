class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs)==1:
            return [strs]
    
        strs_list = [(s, ''.join(sorted(list(s)))) for s in strs]

        strs_dict = {}
        for s in strs_list:
            strs_dict[s[1]] = strs_dict.get(s[1], [])+[s[0]]

        return [s[1] for s in strs_dict.items()]
      
# 133 ms
