def solution(str1, str2):
    from collections import Counter

    str1, str2 = str1.lower(), str2.lower()
    strs1 = [str1[i:i + 2] for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    strs2 = [str2[i:i + 2] for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]
    print(strs1, strs2)

    if not strs1 and not strs2:
        return 65536

    set1 = set([f'{k}{i+1}' for k, v in Counter(strs1).items() for i in range(v)])
    set2 = set([f'{k}{i + 1}' for k, v in Counter(strs2).items() for i in range(v)])

    inter = set1 and set2
    union = set1 or set2
    print(inter, union)

    return int(len(inter) / len(union) * 65536)
  
  # 위 함수보다 간결
  # Counter() 딕셔너리 자체로 합집합, 교집합 계산 가능
  def solution(str1, str2):
    from collections import Counter

    str1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    if len(str1) == 0 and len(str2) == 0:
        return 65536

    c1, c2 = Counter(str1), Counter(str2)

    de = sum((c1 | c2).values())  # 합집합: c1 or c2
    nu = sum((c1 & c2).values())  # 교집합: c1 and c2

    return int(nu / de * 65536)
