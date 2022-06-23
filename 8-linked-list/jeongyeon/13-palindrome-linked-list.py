'''
리스트로 변환

Runtime: 1304 ms
Memory: 47.6 MB
'''

def isPalindrome_tolist(head) -> bool:
    head_list = []

    if not head:
        return True

    node = head
    while node is not None:
        head_list.append(node.val)
        node = node.next

    # 홀수 팰린드롬인 경우를 고려하여 idx 지정
    while len(head_list) > 1:
        if head_list.pop(0) != head_list.pop():
            return False
    return True

'''
deque로 변환 변환

Runtime: 974 ms
Memory: 47.7 MB
'''

def isPalindrome_use_deque(head):
    from collections import deque

    if not head:
        return True

    head_deque = deque()
    node = head
    while node is not None:
        head_deque.append(node.val)
        node = node.next

    while len(head_deque) > 1:
        if head_deque.popleft() != head_deque.pop():
            return False
    return True

'''
runner 이용

Runtime: 943 ms
Memory: 31.2 MB
'''
def isPalindrome_use_runner(head):
    if not head:
        return True

    rev = None
    fast = slow = head

    # fast는 두 칸씩 건너뛰기 때문에 fast, fast.next 모두 not None 이어야 함
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    # 홀수 팰린드롬인 case, slow가 중간값을 가르키므로 한 칸 이동
    if fast:
        slow = slow.next

    # Check palindrome
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not slow


