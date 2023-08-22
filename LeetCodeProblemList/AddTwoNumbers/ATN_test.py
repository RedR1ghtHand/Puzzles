from LeetCodeProblemList.AddTwoNumbers.ATN import ListNode, addTwoNumbers


class TestAddTwoNumbers:
    case_1 = [
        ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))),
        ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    ]
    case_2 = [
        ListNode(val=9, next=ListNode(val=9, next=ListNode(
            val=9, next=ListNode(val=9, next=ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9))))
        ))),
        ListNode(val=9, next=ListNode(val=9, next=ListNode(
            val=9, next=ListNode(val=9)
        )))
    ]

    def test_case_1(self):
        expected = [7, 0, 8]
        result = addTwoNumbers(*self.case_1)

        for item in expected:
            assert item == result.val
            result = result.next

    def test_case_2(self):
        expected = [8, 9, 9, 9, 0, 0, 0, 1]
        result = addTwoNumbers(*self.case_2)

        for item in expected:
            assert item == result.val
            result = result.next
