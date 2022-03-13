class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        max_possible = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == 0 or (i >= 1 and flowerbed[i - 1] == 0)) and ( i == len(flowerbed) - 1 or (
                        i <= len(flowerbed) - 1 and flowerbed[i + 1] == 0)):
                    max_possible += 1
                    flowerbed[i] = 1
        if max_possible >= n:
            return True
        else:
            return False
