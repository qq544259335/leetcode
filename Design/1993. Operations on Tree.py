class LockingTree:
    lockCondition = []
    treeNode = []
    desDict = {}

    def __init__(self, parent: [int]):
        self.treeNode = parent
        for i in range(len(parent) - 1, 0, -1):
            pos = i
            if pos not in self.desDict.keys():
                self.desDict[pos] = []
            while pos != - 1:
                if parent[0][pos] in self.desDict.keys():
                    for p in self.desDict[pos]:
                        if p not in self.desDict[parent[pos]]:
                            self.desDict[parent[pos]].append(p)
                else:
                    self.desDict[parent[pos]] = [pos]
                pos = parent[pos]
        print(self.desDict)
        return

    def lock(self, num: int, user: int) -> bool:
        return

    def unlock(self, num: int, user: int) -> bool:
        return

    def upgrade(self, num: int, user: int) -> bool:
        return


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

input = [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
tree = LockingTree(input)
