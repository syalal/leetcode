# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        res = d
        total = carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            n = total % 10
            carry = total // 10
            res.next = ListNode(n)
            res = res.next

        return d.next
        # def get_num(l1):
        #     num = 0
        #     count = 0
        #     curr = l1
        #     while curr.next:
        #         num = num + (10^count)*curr.val
        #         curr = curr.next
        #         count += 1
        #     return num

        # num1 = get_num(l1)
        # num2 = get_num(l2)

        # res_num = num1+num2

        # tmp = res_num
        # res = ListNode()
        # while tmp >=0:
        #     n = tmp%10
        #     res.val = n
        #     tmp = tmp/10 
        
        # return res

            