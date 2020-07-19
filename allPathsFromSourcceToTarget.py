def allPathsSourceTarget(graph):
    
    def solve(node):
        if node == len(graph) - 1:
            return [[len(graph) - 1]]
        
        ans = []
        for nei in graph[node]:
            for path in solve(nei):
                ans.append([node] + path)
        return ans
    
    return solve(0)