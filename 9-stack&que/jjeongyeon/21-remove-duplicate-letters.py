
'''
stack 이용
Runtime : 42 ms
Memory: 13.9 MB
'''

def removeDuplicateLetters(s):
    from collections import Counter
    counter, stack = Counter(s), []
    
    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
        # 현재 문자열이 stack에 마지막 값 보다 사전적으로 앞에 있는데,
        # stack 마지막 값이 뒤에 한 번 더 나오면 -> pop()으로 제거 (뒤에서 다시 stack에 넣어주기 위함)
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)
    
    return ''.join(stack)

  
  
def removeDuplicateLetters(s):
    from collections import Counter
    counter, seen, stack = Counter(s), set(), []
    
    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
        # 현재 문자열이 stack에 마지막 값 보다 사전적으로 앞에 있는데,
        # stack 마지막 값이 뒤에 한 번 더 나오면 -> pop()으로 제거 (뒤에서 다시 stack에 넣어주기 위함)
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    
    return ''.join(stack)
