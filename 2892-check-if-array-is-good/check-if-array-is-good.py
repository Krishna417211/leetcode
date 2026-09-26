class Solution:
    def isGood(self, nums: List[int]) -> bool:

        count = Counter(nums)

        for i in range(1,len(nums)-1):
            if i not in nums:
                print(i)
                return False
        return count[len(nums)-1] >= 2
        