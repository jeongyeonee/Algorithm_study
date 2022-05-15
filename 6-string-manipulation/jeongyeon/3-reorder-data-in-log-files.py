class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_d = []
        logs_l = []
        for l in logs:
            tmp = l.split()
            if tmp[1].isalpha():
                logs_l.append(tmp)
            else:
                logs_d.append(tmp)

        logs_l = sorted(logs_l, key=lambda x: (x[1:], x[0]))
        return [' '.join(l) for l in logs_l] + [' '.join(l) for l in logs_d]
      
# 60 ms

'''
split -> join으로 불필요한 연산 시행

split하지 않은 문자열을 이용하여
lambda x: (x.split()[1:], x.split()[0]) 했으면 46 ms
'''
