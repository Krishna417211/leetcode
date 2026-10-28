class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""


        if numRows == 1:
            return s

        for r in range(numRows):

            increment = (numRows - 1) * 2

            for i in range(r, len(s), increment):
                res += s[i]

                if (r > 0 and r < numRows - 1 and increment + i - 2 * r < len(s)):
                    res += s[increment + i - 2 * r]

        return res



            