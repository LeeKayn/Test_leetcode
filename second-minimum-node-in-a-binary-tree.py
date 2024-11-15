"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root):
        # Initialize a set to store unique values
        unique_values = set()

        # Helper function to perform DFS
        def dfs(node):
            if node:
                unique_values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        # Perform DFS starting from the root
        dfs(root)

        # If there are less than two unique values, return -1
        if len(unique_values) < 2:
            return -1

        # Return the second smallest value
        return sorted(unique_values)[1]