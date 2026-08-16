class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        group = defaultdict(list)

        for u, v in edges:
            group[u].append(v)
            group[v].append(u)

        visited = set()
        cnt = 0
        queue = deque()
        for i in range(n):
            if i in visited:
                continue
            else:
                cnt += 1
                visited.add(i)
                queue.append(i)

            while queue:
                u = queue.popleft()
                for v in group[u]:
                    if v not in visited:
                        queue.append(v)
                        visited.add(v)


        return cnt


