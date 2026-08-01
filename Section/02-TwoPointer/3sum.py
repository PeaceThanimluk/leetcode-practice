'''
Start
    หา3ตัวเลขที่รวมกันได้ 0 
    รับ่ค่ามาเป็น list[number]
    sort list

    สร้างค่า left = 0 right = len(list) - 1
'''

class Solution:
    def threeSum(self, nums):
        nums.sort()
        sum_list = []

        for index in range(len(nums)):
            left = index + 1
            right = len(nums) - 1

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            while left < right:
                sum_result = nums[index] + nums[left] + nums[right]

                if sum_result == 0:
                        sum_list.append([nums[index], nums[left], nums[right]])
                        left += 1 
                        right -=1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                elif sum_result < 0:
                     left += 1
                elif sum_result > 0:
                     right -= 1

        return sum_list


newSolution = Solution()
print(newSolution.threeSum([-1,0,1,2,-1,-4]))