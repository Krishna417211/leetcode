class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = Counter(nums)

        for i,val in a.items():
            if val > len(nums)//2:
                return i