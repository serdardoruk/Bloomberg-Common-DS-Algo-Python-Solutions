'''
Given a list of meetings for a given day in a conference center, return a list
of time slots during which the most number of concurrent meetings are held.
Each meeting has a start time and end time and occupies a single room in a
conference center.

Input:
(100,300) // meeting 1, 1:00 am to 3:00 am
(145,215) // meeting 2
(200,230) // meeting 3
(215,300) // meeting 4
(215,400) // meeting 5
(500,600) // meeting 6
(600,700) // meeting 7

Output:
(215,230) // 4 concurrent meetings: 1,3,4,5

Last question in my second round onsite interview, could not figure this out for the life of me. 
This was for New Grad NYC position. I can write up a full onsite experience if requested.
'''
import heapq
def meeting_rooms(meetings):
    meetings = sorted(meetings, key=lambda k:k[1])
    
    heap = [(meetings[0][1], 0)]
    
    overlaps = {}
    
    for i in range(1, len(meetings)):
        if meetings[i][0] < heap[0][0]:
            heapq.heappush(heap, (meetings[i][1], i))
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, (meetings[i][1], i))
        
        if meetings[i][0] < heap[0][0]:
            p = (meetings[i][0], heap[0][0])
            if p in overlaps:
                overlaps[p] = max(overlaps[p], len(heap))
            else:
                overlaps[p] = len(heap)
    
    return [x for x, y in overlaps.items() if y == max(overlaps.values())]


meetings = [(100,300),
(145,215),
(200,230),
(215,300),
(215,400),
(500,600),
(600,700)]

print(meeting_rooms(meetings))