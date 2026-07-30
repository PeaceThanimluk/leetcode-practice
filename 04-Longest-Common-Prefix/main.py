'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

#หาคำนำหน้าที่มีกันทุกคำ

class Solution:
    def longestCommonPrefix(self, stringList):
        prefix = stringList[0]

        for i in range(1, len(stringList)):
            current = stringList[i]
            sameLetter = ""

            for letter in range(min(len(prefix), len(current))):
                if prefix[letter] == current[letter]:
                    sameLetter += prefix[letter]
                else:
                    break

            prefix = sameLetter

        return prefix


newSolution = Solution()
print(newSolution.longestCommonPrefix(["flower", "flow", "flight"]))
