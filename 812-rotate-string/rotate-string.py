class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        s = list(s)
        goal = list(goal)

        if Counter(s) != Counter(goal):
            return False

        for _ in range(len(s)):
            for i in range(1,len(s)):
                s[i],s[i-1] = s[i-1],s[i]

            if s == goal:
                return True

        return False

        