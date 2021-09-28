class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)

        for i in range(m):
            mat[i] = set(mat[i])  # remove duplicates

        self.min_diff = inf

        @cache
        def search(i, s):
            if target + self.min_diff < s:  # sum is too big
                return inf
            if i == m:
                return abs(target - s)

            row = mat[i]
            min_diff = inf
            for num in row:
                min_diff = min(min_diff, search(i + 1, s + num))

            self.min_diff = min(self.min_diff, min_diff)

            return min_diff

        return search(0, 0)