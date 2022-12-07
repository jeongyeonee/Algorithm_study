'''
Stack 이용 X
Rumtime : 77 ms
Memory : 13.8 MB
'''

def isValid_nostack(s):
    while s:
        l = len(s)
        s = s.replace('{}', '').replace('()','').replace('[]', '')
        # replace 된 문자열이 없으면 return False 
        if len(s)==l:
            return False
    return len(s)==0


'''
Stack 이용
Runtime : 47 ms
Memory : 13.9 MB
'''

def isValid(s):
    dic = {'}':'{', 
           ')':'(', 
           ']':'['}
    stack = []
    
    for char in s:
        if char not in dic:
            stack.append(char)
        elif stack.pop() != dic[char]:
            return False
    return len(stack) == 0


