#BFS + mean heap (priority queue)

from queue import PriorityQueue
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        answer = [0] * len(queries)
        queue = deque()
        queue.append((0, 0))
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1

        queries = list(enumerate(queries))
        queries.sort(key=lambda x: x[1])
        #print(queries)
        point = 0
        dir_xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pq = PriorityQueue()
        pq.put((grid[0][0], 0, 0))
        #print("I added 0 0")
        for ind, q in queries:
            #if grid[0][0] < q:
            while pq.queue and pq.queue[0][0] < q:
                val, x, y = pq.get()
                #print("I removed", val, x, y)
                point += 1
                for plus_x, plus_y in dir_xy:
                    new_x = x + plus_x
                    new_y = y + plus_y
                    if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y]:
                            #print("I added", grid[new_x][new_y], new_x, new_y)
                            pq.put((grid[new_x][new_y], new_x, new_y))
                            visited[new_x][new_y] = 1     
            answer[ind] = point
        return answer