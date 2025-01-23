class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        index_ans = 0
        intervals = sorted(intervals)
        ans = [intervals[0]]
        for index in range(1, len(intervals)):
            if ans[index_ans][1] >= intervals[index][0]:
                # check which should be the left element
                left = intervals[index][0] if intervals[index][0] < ans[index_ans][0] else ans[index_ans][0]
                right = intervals[index][1] if intervals[index][1] > ans[index_ans][1] else ans[index_ans][1]
                ans[index_ans] = [left, right]
            else:
                index_ans += 1
                ans.append(intervals[index])
        return ans
