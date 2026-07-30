class Solution:
    def longestCommonPrefix(self, listWord):
        prefix = listWord[0]

        for i in range(1, len(listWord)):
            current = listWord[i]
            sameLetter = ""

            for letter in range(min(len(prefix), len(current))):
                if prefix[letter] == current[letter]:
                    sameLetter += prefix[letter]
                else:
                    break

            prefix = sameLetter

        print(prefix)
        return prefix
    


newSolution = Solution()
newSolution.longestCommonPrefix(["lemon","lemen","lomen"])