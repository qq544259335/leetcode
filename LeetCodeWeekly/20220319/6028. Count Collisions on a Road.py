class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = list(directions)
        i = 0
        res = 0
        while i < len(directions) - 1:
            if directions[i] == "R":
                if directions[i + 1] == "S":
                    res += 1
                    directions[i] = "S"
                    i -= 2
                elif directions[i + 1] == "L":
                    res += 2
                    directions[i] = "S"
                    directions[i + 1] = "S"
                    i -= 2
            elif directions[i] == "S" and directions[i + 1] == "L":
                res += 1
                directions[i + 1] = "S"
            i += 1
            i = i if i > 0 else 0
        return res