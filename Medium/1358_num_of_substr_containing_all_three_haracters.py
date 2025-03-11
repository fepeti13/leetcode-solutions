class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d= {"a": 0, "b": 0, "c": 0}
        n = len(s)
        sol = 0
        l = 0
        for r in range(0, n):
            d[s[r]] += 1
            while d["a"] != 0 and d["b"] != 0 and d["c"] != 0:
                sol += n - r
                d[s[l]] -= 1
                l += 1

        return sol