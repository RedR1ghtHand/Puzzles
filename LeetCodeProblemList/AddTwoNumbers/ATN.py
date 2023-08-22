from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    res = ListNode(0)
    case = res

    while l1 or l2 or carry:
        num_1 = l1.val if l1 else 0
        num_2 = l2.val if l2 else 0

        sum_val = num_1 + num_2 + carry
        carry = sum_val // 10
        num = sum_val % 10

        case.next = ListNode(num)
        case = case.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return res.next
