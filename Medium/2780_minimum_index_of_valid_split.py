#the first method is with built in python counter method, to determine the dominant element
#the second one is with Boyer-Moore Majority Vote Algorithm

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #counts = Counter(nums)
        #dominant, count = counts.most_common(1)[0]
        
        candidate = None
        count = 1
        for i in nums:
            if i == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = i
                count = 1
        dominant = candidate
        count = 0
        for i in nums:
            if i == dominant:
                count += 1   

        print(dominant, count)
        if count < len(nums)/2 + 1:
            return -1
        count = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                count += 1
            if count > (i+1)/2:
                #print(count, i)
                return i
        return -1
