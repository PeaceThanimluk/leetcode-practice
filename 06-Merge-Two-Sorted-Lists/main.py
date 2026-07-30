'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

'''
Peseudo

Start
    สร้าง init
    รับค่า2ค่าเป็น list คือ list1 list2


'''

class ListNodes:
    def __init__(self, val = 0, Next = None):
        self.value = val
        self.next = Next

class Solution:
    def mergeTwoList(self, list1, list2):
        pass
        
