__author__ = 'HsinYeh Lin'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = 0
        nextA = headA
        lenB = 0
        nextB = headB
        while nextA != None:
            nextA = nextA.next
            lenA += 1
        while nextB != None:
            nextB = nextB.next
            lenB += 1

        new_headA = headA
        new_headB = headB
        if lenA > lenB:
            #drop the first few elements of list A
            temp = lenA - lenB
            for i in range(temp):
                new_headA = new_headA.next
                i += 1
        elif lenA < lenB:
            #drop the first few elements of list B
            temp = lenB - lenA
            for i in range(temp):
                new_headB = new_headB.next
                i += 1

        while new_headA != None and new_headB != None:
            if new_headA == new_headB:
                return new_headA
            else:
                new_headA = new_headA.next
                new_headB = new_headB.next
        return None