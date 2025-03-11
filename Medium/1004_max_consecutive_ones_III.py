#better solution

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, zeros, max_length = 0, 0, 0
        for r in range(0, len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
        
            max_length = max(max_length, r - l + 1)
        return max_length