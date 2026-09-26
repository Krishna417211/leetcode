class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        val = []

        for i in nums:
            
                for j in str(i):
                    val.append(int(j))

            
        return val
        