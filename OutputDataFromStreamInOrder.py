'''
https://leetcode.com/discuss/interview-question/314733/Bloomberg-or-Output-data-from-a-stream-in-order

There is a continous stream of data in the form of:
Input: (1, "abcd"), (2, "efgh"), (4, "mnop"), (5, "qrst"), (3, "ijkl")

Write a program to output the data from the stream in realtime in order, so 1,2,3,4,5..
You cannot queue up the incoming data from the stream.
So for example if the first incoming bit of data is (1, "abcd"), and the second is (4, "mnop"), you cannot output (4, "mnop") until you get 2, 3.

'''
# import heapq
# class StreamData:
#     def __init__(self):
#         self.heap = []
#         self.lastOutput = 0

#     def addData(self, data):
#         heapq.heappush(self.heap, data)
    
#     def returnData(self):
#         numToOutput = None
#         if self.heap and self.heap[0][0] == self.lastOutput + 1:
#             numToOutput = heapq.heappop(self.heap)
#             self.lastOutput = numToOutput[0]
#         return numToOutput[1] if numToOutput != None

# myStream = StreamData()
# myStream.addData((1, "abcd"))
# myStream.addData((2, "efgh"))
# print(myStream.returnData())
# print(myStream.returnData())
# print(myStream.returnData())
# print(myStream.returnData())
# myStream.addData((4, "mnop"))
# myStream.addData((5, "qrst"))
# myStream.addData((3, "ijkl"))
# print(myStream.returnData())
# print(myStream.returnData())
# print(myStream.returnData())
# print(myStream.returnData())



class StreamData:
    def __init__(self):
        self.dict = {}
        self.lastOutput = 0

    def addData(self, data):
        self.dict[data[0]] = data
    
    def returnData(self):
        numToOutput = None
        if self.lastOutput + 1 in self.dict:
            numToOutput = self.dict[self.lastOutput + 1]
            del self.dict[self.lastOutput + 1]
            self.lastOutput += 1
        return numToOutput


myStream = StreamData()
myStream.addData((1, "abcd"))
myStream.addData((2, "efgh"))
print(myStream.returnData())
print(myStream.returnData())
print(myStream.returnData())
print(myStream.returnData())
myStream.addData((4, "mnop"))
myStream.addData((5, "qrst"))
myStream.addData((3, "ijkl"))
print(myStream.returnData())
print(myStream.returnData())
print(myStream.returnData())
print(myStream.returnData())
