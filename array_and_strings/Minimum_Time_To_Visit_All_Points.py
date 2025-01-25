class Solution:
    def minTimeToVisitAllPoints(self, points):
        x_cord, y_cord = points[0]
        time = 0
        for index in range(1, len(points)):
            x2, y2 = points[index]
            time += max(abs(x2 - x_cord), abs(y2 - y_cord))
            x_cord, y_cord = x2, y2
        return time
