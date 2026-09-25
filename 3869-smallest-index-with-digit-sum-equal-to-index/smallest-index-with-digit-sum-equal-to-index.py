class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if len(str(nums[i])) > 1:
                sum_ = 0
                for j in str(nums[i]):
                    sum_ += int(j)

                if i == sum_:
                    return i
            elif i == nums[i]:
                return i

        return -1            
        