from collections import deque


def num_islands(grid):
    if not grid:
        return 0

    h = len(grid)
    w = len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        q = deque()
        visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.pop()
            directions = [
                (1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (-1, 1), (1, -1), (-1, -1)
            ]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (
                        r in range(h) and
                        c in range(w) and
                        grid[r][c] == '1' and
                        (r, c) not in visit
                ):
                    visit.add((r, c))
                    q.append((r, c))

    for r in range(h):
        for c in range(w):
            if grid[r][c] == '1' and (r, c) not in visit:
                bfs(r, c)
                islands += 1

    return islands
