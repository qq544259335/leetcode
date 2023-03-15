class Solution:
    def possibleBipartition(self, n: int, dislikes: [[int]]) -> bool:
        group_a, group_b = set(), set()
        group_a.add(1)
        for a, b in dislikes:
            