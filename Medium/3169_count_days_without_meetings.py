#merge intervals

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        #print(meetings)
        count = meetings[0][0] - 1
        #print(count)

        last_end = meetings[0][1]
        for start, end in meetings[1:]:
            if start <= last_end:
                last_end = max(last_end, end)
            else:
                count = count + start - last_end - 1
                #print(last_end, start, count)
                last_end = end

        count += days - last_end
        return count