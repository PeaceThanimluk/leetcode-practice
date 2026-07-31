'''
Start
    input มี2ค่าคือ list[int] และ k = จำนวนสัญลักษณ์เลขที่ซ้ำกัน k อันดับ เช่น 2 -> 2อันดับ
    สร้าง dictionary เอาไว้เก็บตัวเลข
    เช่น [1,1,1,2,2,3]
    {
        1: 3,
        2: 2,
        3: 1,
    } 

    loop ด้วย .item
        สร้าง lsit ขึ้นมาเพื่อเก็บ key


'''

class Solution:
    def topKFrequent(self, nums, k):
        frequency = {}

        for number in nums:
            if number not in frequency:
                frequency[number] = 1
            else:
                frequency[number] += 1

        local_list = []

        for key, value in frequency.items():
            local_list.append((key, value))

        new_list = sorted(
            frequency.items(),
            key=lambda item: item[1],
            reverse=True
        )


        select = new_list[:k]
        result = []

        for key in select:
            result.append(key[0])

        return result

newSolution = Solution()
print(newSolution.topKFrequent([4,1,-1,2,-1,2,3], 2))