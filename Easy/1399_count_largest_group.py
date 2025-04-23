class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = [0 for _ in range(1, 38)]
        for i in range (1, n+1):
            sum = 0
            while i > 0:
                sum += i%10
                i = i // 10
            count[sum] += 1

        count_max = 0
        for i in range(1, 37):
            if count[i] == max(count):
                count_max +=1

        return count_max