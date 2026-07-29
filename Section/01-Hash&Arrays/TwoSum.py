'''
Start
    input รับมา2ค่า คือ numsList , target 
    [3, 2, 4] target คือ 5
    สร้าง dict seen
    สร้างตัวแปร complement = target - number (5 - 3)
    ถ้า complement มีอยู่ใน seen return [number, complement]
    ถ้า complement ไม่อยู่ใน seen -> seen[nums] = i


'''


class Solution:
    def TwoSum(self, nums, target):
        seen = {}

        for i, number in enumerate(nums):
            complement = target - number

            if complement in seen:
                return [number, complement]

            seen[number] = i

newSolution = Solution()
print(newSolution.TwoSum([3, 2, 4], 6))