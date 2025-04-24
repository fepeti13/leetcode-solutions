class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))
        left = 0
        hmp = {}
        sol = 0
        for right in range(0, len(nums)):
            hmp[nums[right]] = hmp.get(nums[right], 0) + 1
            while len(hmp) == distinct_count:
                sol += len(nums) - right
                hmp[nums[left]] -= 1
                if hmp[nums[left]] == 0:
                    del hmp[nums[left]]
                left += 1

        return sol