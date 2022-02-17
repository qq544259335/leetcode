class Solution:
    def pivotArray(self, nums: [int], pivot: int) -> [int]:
        smalls = []
        bigs = []
        equals = []
        for n in nums:
            if n == pivot:
                equals.append(n)
            elif n > pivot:
                bigs.append(n)
            else:
                smalls.append(n)
        return smalls + equals + bigs
