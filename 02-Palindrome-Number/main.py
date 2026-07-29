class Solution:
    def isPalindrome(self, x : int) -> bool:
        s = str(x)
        return s == s[::-1] #กลับลำดับ
    
newSolution = Solution()

print(newSolution.isPalindrome(1001))

