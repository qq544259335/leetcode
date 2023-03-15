class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        class UnionFind:
            def __init__(self, v):
                self.val = v
                self.parent = self

            def find_parent(self):
                if self.parent.val != self.val:
                    return self.parent.find_parent()
                else:
                    return self.val

            def union(self , a, b):
                pa = a.find_parent()
                pb = b.find_parent()