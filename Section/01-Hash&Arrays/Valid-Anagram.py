'''
Start
    input รับค่ามา 2 string = fristString secondString
    ถ้า len s != len t return false
    สร้าง dict ขึ้นมาเก็บจำนวนตัวอักษร s a = 2 n = 1
    สร้าง dict ขึ้นมาเก็บจำนวนตัวอักษร t a = 2 n = 1
    loop ด้วยความยาวstring ของ s เพื่อเก็บจำนวนของตัวอักษรก่อน
        ถ้าตัวอักษรยังไม่อยู่ใน dict -> dict[ตัวอักษร] = 1
        ถ้าตัวอักษรอยู่ใน dict -> dict[ตัวอักษร] += 1
    loop ด้วยความยาว string ของ t เพื่อเก็บจำนวนตัวอักษร เหมือน s
    
    ถ้า dict s == dict t return true else return false
        
    
'''

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t): return False

        dictS = {}
        dictT = {}

        for i in range(len(s)):
            text = s[i]
            if not text in dictS:
                dictS[text] = 1
            else:
                dictS[text] += 1

        for i in range(len(t)):
            text = t[i]

            if not text in dictT:
                dictT[text] = 1
            else:
                dictT[text] += 1

        if dictS == dictT:
            return True
        else:
            return False

newSolution = Solution()
print(newSolution.isAnagram("anagram", "nagarem"))