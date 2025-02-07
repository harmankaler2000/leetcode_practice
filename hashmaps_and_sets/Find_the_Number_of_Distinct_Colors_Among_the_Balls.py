class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colour_map = {}
        ball_count = Counter()
        ans = []
        for x, y in queries:
            ball_count[y] += 1
            if x in colour_map:
                ball_count[colour_map[x]] -= 1
                if ball_count[colour_map[x]] == 0:
                    ball_count.pop(colour_map[x])
            colour_map[x] = y
            ans.append(len(ball_count))
        return ans
