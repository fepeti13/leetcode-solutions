#own solution

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        zeros = 0
        max_length = 0
        while r < len(nums):
            if nums[r] == 0:
                if(zeros == k):
                    while nums[l] != 0:
                        l += 1
                    l += 1
                else:
                    zeros += 1
            if( r - l + 1 > max_length):
                max_length = r - l + 1
            print(l, r, zeros)       
            r+=1
        
        return max_length