class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        b = []
        for i in range(len(nums)-1,-1,-1):
            b.append(nums[i])

        return nums + b