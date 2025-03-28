class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        y = []
        x = []
        for points in rectangles:
            x.append([points[0], points[2]])
            y.append([points[1], points[3]])

        x.sort(key = lambda a: a[0])
        y.sort(key = lambda a: a[0])

        sol = 0
        last_end = x[0][1]
        for start, end in x[1:]:
            if start < last_end:
                last_end = max(last_end, end)
            else:
                sol += 1
                last_end = end
                if sol == 2:
                    return True
        
        sol = 0
        last_end = y[0][1]
        for start, end in y[1:]:
            if start < last_end:
                last_end = max(last_end, end)
            else:
                sol += 1
                last_end = end
                if sol == 2:
                    return True
        
        return False