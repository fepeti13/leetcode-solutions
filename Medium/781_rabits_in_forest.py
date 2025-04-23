class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits_count = 0
        counter = Counter(answers)
        for key in counter:
            rabbits_count += ceil(counter[key] / (key + 1)) * (key + 1)

        return rabbits_count