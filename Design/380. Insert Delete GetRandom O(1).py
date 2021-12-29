import random
# https://leetcode.com/problems/insert-delete-getrandom-o1/solution/
class RandomizedSet:
    def __init__(self):
        self.self_dict = {}
        self.self_list = []
    def insert(self, val: int) -> bool:
        if self.self_dict.get(val) is not None:
            return False
        else:
            self.self_dict[val] = len(self.self_list)
            self.self_list.append(val)
            return True
    def remove(self, val: int) -> bool:
        if self.self_dict.get(val) is not None:
            index = self.self_dict.get(val)
            self.self_list[-1], self.self_list[index] = self.self_list[index], self.self_list[-1]
            self.self_dict[self.self_list[index]] = index
            self.self_list.pop(-1)
            del self.self_dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        # return self.self_list[random.randint(0, len(self.self_list) - 1)]
        return random.choice(self.self_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
