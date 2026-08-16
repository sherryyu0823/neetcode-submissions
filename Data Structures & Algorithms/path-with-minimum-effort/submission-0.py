class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        dist = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = {}
        heap = [(0, 0, 0)]

        r = len(heights)
        c = len(heights[0])
        while heap:
            e, x, y = heapq.heappop(heap)
            if (x, y) in visited: continue

            visited[(x, y)] = e
            if x==r-1 and y == c-1: return max(visited.values())

            for dx, dy in dist:
                nx = x+dx
                ny = y+dy

                if 0<= nx <r and 0<=ny<c:
                    heapq.heappush(heap, (abs(heights[x][y]-heights[nx][ny]), nx, ny))

