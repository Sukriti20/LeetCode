# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        if(root==None):
                return 0
        else:
            q.append({'node':root,'depth':1})
            while len(q)>0:
                ele = q.pop(0)
                node=ele['node']
                depth=ele['depth']
                if node.left == None and node.right == None:
                    return depth
                if (node.left) != None:
                    q.append({'node':node.left,'depth':depth+1})
                if node.right != None:
                    q.append({'node':node.right,'depth':depth+1})
                