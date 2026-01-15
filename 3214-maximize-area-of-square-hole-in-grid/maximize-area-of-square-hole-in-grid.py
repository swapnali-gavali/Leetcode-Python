class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """

        def max_consecutive(bars):
            bars.sort()
            longest = 1
            current = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current += 1
                    longest = max(longest, current)
                else:
                    current = 1

            return longest

        max_h = max_consecutive(hBars)
        max_v = max_consecutive(vBars)

        side = min(max_h + 1, max_v + 1)
        return side * side
