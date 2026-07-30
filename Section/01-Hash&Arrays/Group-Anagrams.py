'''
Start
    ตัวอย่าง input ["eat","tea","tan","ate","nat","bat"]
    output ที่ต้องได้ : [["bat"],["nat","tan"],["ate","eat","tea"]]

    input รับค่าเป็น list[string] 
    สร้าง object เอาไว้เก็บkey และเอาไว้ตรวจสอบว่ามีคำไหนตรงกับ key บ้าง
    สร้าง list เอาไว้เก็บคำที่่ได้มาแล้ว

    loop ด้วยความยาว list for word in stringList
        ต้องเรียงลำดับตัวอักษรก่อนเช่นจาก bat ให้กลายเป็น abt คำอื่นๆจะได้keyตรงกัน
        ถ้าคำที่เรียงมาแล้ว(key) ยังไม่อยุ่ object ให้เพิ่ม key : [word] -> list
        ถ้าอยู่แล้วให้value ของ key append คำใหม่ที่ key ตรงกัน

    ต่อไปจะเอาvalue ทั้งหมดที่อยู่ใน object เข้าไปใส่ใน list

    loop ด้วย object.item() -> for key,value in object.item()
        list.append(value)

    แต่list ยังไม่เรียงลำดับจำนวนความยาว list ดังนั้นเราจึงใช้ list.sort(key=len) 
    return list

'''

class Solution:
    def groupAnagrams(self, strings):
        word_object = {} 
        list_anagram = []

        for word in strings:
            char = list(word)
            char.sort()
            key = "".join(char)

            if not key in word_object:
                word_object[key] = [word]
            else:
                word_object[key].append(word)

        for key,value in word_object.items():
            list_anagram.append(value)

        list_anagram.sort(key=len)
        return list_anagram

newSolution = Solution()
print(newSolution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))