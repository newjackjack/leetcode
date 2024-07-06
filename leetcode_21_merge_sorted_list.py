from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1 and list2 are heads
        # create a dummy head for the merged linked list
        # and a current pointer to keep track of the current node
        merged_head = ListNode()
        current = merged_head

        while list1 and list2:
            # if list1.val > list2.val => move current.next to list2
            if(list1.val > list2.val):
                current.next = list2
                # increment list2 to list2.next
                list2 = list2.next

            # else list1.val <= list2.val => point current.next to the list1
            else:
                
                current.next = list1
                # increment list1 to list1.next
                list1 = list1.next
            # after moving current.next to the smaller list head
            # => move current to current.next
            current = current.next

        # length of list1 > list2 -> the rest is list1
        if list1:
            current.next = list1
        # length of list1 < list2 -> the rest is list2
        else:
            current.next = list2

        return merged_head.next
