class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        val = []

        for i in nums:
            if len(str(i)) > 1:
                for j in str(i):
                    val.append(int(j))

            else:
                val.append(i)

        return val
        