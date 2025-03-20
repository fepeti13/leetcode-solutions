class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range (0, n-2):
            if(nums[i]==0):
                nums[i]=1
                nums[i+1] = (nums[i+1] + 1) % 2
                nums[i+2] = (nums[i+2] + 1) % 2
                count += 1

        if nums[n-2]==0 or nums[n-1]==0:
            return -1
        return count
