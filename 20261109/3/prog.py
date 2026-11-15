from collections import deque


class Maze:
    def __init__(self, N):
        self.N = N
        self.open_edges = set()

    def _edge(self, x1, y1, x2, y2):
        p1 = (x1, y1)
        p2 = (x2, y2)
        return (p1, p2) if p1 <= p2 else (p2, p1)

    def _parse_key(self, key):
        x0, sl, y1 = key
        y0 = sl.start
        x1 = sl.stop
        return x0, y0, x1, y1

    def __setitem__(self, key, value):
        x0, y0, x1, y1 = self._parse_key(key)

        if x0 == x1:
            step = 1 if y1 >= y0 else -1
            for y in range(y0, y1, step):
                e = self._edge(x0, y, x0, y + step)
                if value == "·":
                    self.open_edges.add(e)
                elif value == "█":
                    self.open_edges.discard(e)

        elif y0 == y1:
            step = 1 if x1 >= x0 else -1
            for x in range(x0, x1, step):
                e = self._edge(x, y0, x + step, y0)
                if value == "·":
                    self.open_edges.add(e)
                elif value == "█":
                    self.open_edges.discard(e)

    def __getitem__(self, key):
        x0, y0, x1, y1 = self._parse_key(key)

        q = deque([(x0, y0)])
        seen = {(x0, y0)}

        while q:
            x, y = q.popleft()

            if (x, y) == (x1, y1):
                return True

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy

                if not (0 <= nx < self.N and 0 <= ny < self.N):
                    continue

                if (nx, ny) in seen:
                    continue

                if self._edge(x, y, nx, ny) in self.open_edges:
                    seen.add((nx, ny))
                    q.append((nx, ny))

        return False

    def __str__(self):
        n = self.N
        size = 2 * n + 1

        grid = [["█"] * size for _ in range(size)]

        for y in range(n):
            for x in range(n):
                grid[2 * y + 1][2 * x + 1] = "·"

        for p1, p2 in self.open_edges:
            x1, y1 = p1
            x2, y2 = p2

            if y1 == y2:
                x = min(x1, x2)
                grid[2 * y1 + 1][2 * x + 2] = "·"
            else:
                y = min(y1, y2)
                grid[2 * y + 2][2 * x1 + 1] = "·"

        return "\n".join("".join(row) for row in grid)

if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())
