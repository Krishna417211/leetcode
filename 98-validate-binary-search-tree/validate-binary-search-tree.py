# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:


        val = []


        def order(root):
            if not root:
                return []

            order(root.left)
            val.append(root.val)
            order(root.right)

            return val

        order(root)

        for i in range(1, len(val)):
            if val[i-1] >= val[i]:
                return False

        return True

        