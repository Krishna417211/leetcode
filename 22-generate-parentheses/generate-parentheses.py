class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def generate(current, opencount, closecount):

            if len(current) ==  2 * n:
                result.append(current)
                return 

            
            if opencount < n:
                generate(current + '(', opencount + 1, closecount)

            if closecount < opencount:
                generate(current + ')', opencount, closecount + 1)

            return result

        generate('',0,0)

        return result