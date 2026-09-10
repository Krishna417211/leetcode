class Solution:
    def convertToBase7(self, num: int) -> str:

            rem = 0
            val = ''

            if num == 0:
                return '0'

            negative = num < 0
            num = abs(num)

            while num != 0:
                quo = num//7
                rem = num%7
                num = quo

                val += str(rem)

            val = val[::-1]

            if negative:
                val = '-'+ val

            return val