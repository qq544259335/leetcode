class Bitset:

    def __init__(self, size: int):
        self.bit = "0" * size
        self.count_num = 0
        self.flip_bool = False

    def fix(self, idx: int) -> None:
        if (self.bit[idx] != "1" and not self.flip_bool) or (self.bit[idx] == "1" and self.flip_bool):
            add = "1" if not self.flip_bool else "0"
            if idx == 0:
                self.bit = add + self.bit[1:]
            elif idx == len(self.bit) - 1:
                self.bit = self.bit[:len(self.bit) - 1] + add
            else:
                self.bit = self.bit[:idx] + add + self.bit[idx + 1:]
            self.count_num += 1


    def unfix(self, idx: int) -> None:
        if (self.bit[idx] != "0" and not self.flip_bool) or (self.bit[idx] == "0" and self.flip_bool):
            add = "0" if not self.flip_bool else "1"
            if idx == 0:
                self.bit = add + self.bit[1:]
            elif idx == len(self.bit) - 1:
                self.bit = self.bit[:len(self.bit) - 1] + add
            else:
                self.bit = self.bit[:idx] + add + self.bit[idx + 1:]
            self.count_num -= 1


    def flip(self) -> None:
        self.flip_bool = True if not self.flip_bool else False
        self.count_num = len(self.bit) - self.count_num

    def all(self) -> bool:
        return self.count_num == len(self.bit)

    def one(self) -> bool:
        return self.count_num >= 1

    def count(self) -> int:
        return self.count_num

    def toString(self) -> str:
        if not self.flip_bool:
            return self.bit
        else:
            temp = ""
            for c in self.bit:
                temp += "0" if c == "1" else "1"
            return temp

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
