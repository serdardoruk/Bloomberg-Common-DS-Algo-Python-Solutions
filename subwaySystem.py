'''
Implement the class UndergroundSystem that supports three methods:

1. checkIn(int id, string stationName, int t)

A customer with id card equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.
2. checkOut(int id, string stationName, int t)

A customer with id card equal to id, gets out from the station stationName at time t.
3. getAverageTime(string startStation, string endStation) 

Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation to endStation that happened directly.
Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at some station, 
then it gets out at time t2 with t2 > t1. All events happen in chronological order.
'''

class UndergroundSystem:

    def __init__(self):
        self.checkInData = {}
        self.travelData = collections.defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInData[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInData.pop(id)
        self.travelData[(startStation, stationName)][0] += t - startTime
        self.travelData[(startStation, stationName)][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalTrips = self.travelData[(startStation, endStation)]
        return totalTime / totalTrips
        
