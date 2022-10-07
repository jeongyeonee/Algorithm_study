'''
전가산기
Runtime: 121 ms
Memory: 13.8 MB
'''

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    root = head = ListNode()

    # l1, l2 모두 끝날때까지 더해져야 하며
    # 모두 더해졌어도 십의자리수가 남아있는 경우를 고려하여 while carry
    carry = 0
    while l1 or l2 or carry:
        # 두 자리 합
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next
