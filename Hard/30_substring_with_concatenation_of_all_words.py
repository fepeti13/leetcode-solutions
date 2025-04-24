class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        reference_map = {}
        for word in words:
            reference_map[word] = reference_map.get(word, 0) + 1

        n = len(words[0])
        N = len(s)

        for offset in range(0, n):

            left = offset
            seen_map = {}

            for right in range(offset, N, n):
                sub = s[right:(right+n)]

                if sub not in reference_map:
                    seen_map = {}
                    left = right + n
                    continue

                seen_map[sub] = seen_map.get(sub, 0) + 1

                while seen_map[sub] > reference_map[sub]:
                    remove_sub = s[left:(left+n)]
                    seen_map[remove_sub] -= 1
                    left += n

                if (seen_map == reference_map):
                    res.append(left)
            
        return res
        