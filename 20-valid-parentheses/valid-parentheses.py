class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {'[':']','{':'}','(':')'}
        stack = []

        for i in s:
            if i in pairs:
                stack.append(i)

            else:
                if not stack:
                    return False
                top = stack.pop()
                if i != pairs[top]:
                    return False

        return len(stack) == 0

