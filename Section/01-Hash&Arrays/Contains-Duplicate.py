'''
Start
    input รับค่าเป็น List[int]
    สร้าง object nums_objects {}
    loop ด้วยจำนวน nums
    ถ้า number ไม่อยู่ใน object ---> เพิ่มเข้าใน object
    ถา้ number อยู่ใน object ---> return true

    return false
'''

class Solution:
    def containsDuplicate(self, nums):
        nums_object =  {}

        for number in range(len(nums)):
            if not nums[number] in nums_object:
                nums_object[nums[number]] = 1
            else:
                return True

        return False

newSolution = Solution()
newSolution.containsDuplicate([1,2,3,1])