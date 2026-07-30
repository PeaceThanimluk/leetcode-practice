'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

'''

#PeseudoCode

'''
กฏ
1.วงเล็บต้องปิดด้วยวงเล็บชนิดเดียวกัน () [] {}
2.วงเล็บต้องเรียงให้ถูกลำดับ
3.

case1. "()"
case2. "()[]"
case3. "([])"

case4. "(}[]"

ทำ case1ก่อน
Start
    ใช้ stack
    สร้าง list เอาไว้ push pop stack
    สร้าง list ที่เก็บ default วงเล็บเปิด ["(", "[", "{"]
    สร้าง list ที่เก็บ default วงเล็บปิด [")", "]", "}"]
    
    สร้าง loop for letter in range(len(word)) ถ้า index 1 ตรงกับ list วงเล็บเปิด
    appendเข้า stack list 

    ต้องเช็คว่า index1 เป็นวงเล็บเปิด index 2 เป็นวงเล็บปิดที่ไม่ตรงกับวงเล็บเปิดจะทำยังไง

'''

class Solution:
    def isValid(self, word):
        stackList = []
        openTag = ["(", "[", "{"]
        closeTag = [")", "]", "}"]
        correctForm = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }


        for i in range(len(word)):
            if word[i] in openTag:
                stackList.append(word[i])
            else:
                if stackList == []:
                    return False
                
                if stackList[-1] == correctForm[word[i]]:
                    stackList.pop()
                else:
                    return False

        if stackList == []: return True


newSolution = Solution()
answer = newSolution.isValid("({})")
print(answer)