class UndergroundSystem:

    def __init__(self):
        self.checkDict = {}
        self.timeDict = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkDict[id] = [(stationName, t)]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.checkDict[id].append((stationName, t))
        checkIn, checkOut = self.checkDict[id]
        station1, time1 = checkIn
        station2, time2 = checkOut
        key = station1 + '!' + station2
        if key not in self.timeDict.keys():
            self.timeDict[key] = [0, 0]
        self.timeDict[key][1] += 1
        self.timeDict[key][0] += time2 - time1
        self.checkDict.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + '!' + endStation
        return  self.timeDict[key][0]/self.timeDict[key][1]