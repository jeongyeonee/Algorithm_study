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
