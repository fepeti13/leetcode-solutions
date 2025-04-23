class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_inter = 0
        min_inter = 0
        my_sum = 0
        for i in differences:
            my_sum += i
            if my_sum < min_inter:
                min_inter = my_sum
            if my_sum > max_inter:
                max_inter = my_sum

        buffer = upper - lower + 1
        real_buffer = max_inter - min_inter
        return max(buffer - real_buffer, 0)