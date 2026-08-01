'''
Start
    input เป็น string 
    แปลง string ให้เป็น lowercase และ เอา space และ special character ออก
    เอา string มาเปรียบเทียบกับ string reverse
    ถ้าไม่เท่ากัน return false
'''

class Solution:
    def isPalindrome(self, string : str) -> bool:
        left = 0
        right = len(string) - 1

        while left < right:
            if not string[left].isalnum():
                left += 1 
                continue

            if not string[right].isalnum():
                right -= 1
                continue

            if string[left].lower() != string[right].lower():
                return False

            left += 1
            right -= 1
        

        return True


newSolution = Solution()
print(newSolution.isPalindrome("A man, a plan, a canal: Panama"))