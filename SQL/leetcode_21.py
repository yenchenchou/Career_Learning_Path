# Merge Two Sorted Lists

# Solution1: First try

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(0)
        p = newList
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        while l1:
            p.next = l1
            p = p.next
            l1 = l1.next
        while l2:
            p.next = l2
            p = p.next
            l2 = l2.next
        return newList.next # [[None], [None]], [[1], [None]], [[1], [1]], [[1,1], [2]], [[1,1], [1,2]]
# Time: O(n+m), Space: O(n+m)


# Solution1.2: Better one
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(0)
        p = newList
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        # if l1:
        #     p.next = l1
        # else:
        #     p.next = l2
        p.next = l1 or l2
        return newList.next # [[None], [None]], [[1], [None]], [[1], [1]], [[1,1], [2]], [[1,1], [1,2]]
# Time: O(n+m), Space: O(n+m)


# Solution2: Recursion