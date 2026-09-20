class Solution:
    def digitFrequencyScore(self, n: int) -> int:

        count = Counter(str(n))
        num = 0

        for k,val in count.items():
            num += (int(k) * val)
        return num




        