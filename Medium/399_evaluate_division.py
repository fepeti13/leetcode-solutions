class Solution:
    def dfs(self, current, target, visited, graph):
        if current not in graph or target not in graph:
            return -1
        if current == target:
            return 1
        
        visited.add(current)

        for neighbour, weight in graph[current].items():
            if neighbour not in visited:
                mult = self.dfs(neighbour, target, visited, graph)
                if mult != -1:
                    return mult * weight

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        res = []
        for (a, b) in queries:
            visited = set()
            res.append(self.dfs(a, b, visited, graph))

        return res
    