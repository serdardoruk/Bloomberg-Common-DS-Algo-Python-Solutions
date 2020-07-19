# class Sea:
#    def hasShips(self, topRight, bottomLeft):

# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

# https://leetcode.com/problems/number-of-ships-in-a-rectangle/

def countShips(sea, topRight, bottomLeft):
    x, y = topRight.x - bottomLeft.x, topRight.y - bottomLeft.y
    if x == y == 0:
        return sea.hasShips(topRight, bottomLeft)
    
    if not sea.hasShips(topRight, bottomLeft):
        return 0
    
    if x > y:
        half = bottomLeft.x + x // 2
        midTopRight = Point(half, topRight.y)
        midBottomLeft = Point(half + 1, bottomLeft.y)
        return countShips(sea, midTopRight, bottomLeft) + countShips(sea, topRight, midBottomLeft)
        
    else:
        half = bottomLeft.y + y // 2
        midTopRight = Point(topRight.x, half)
        midBottomLeft = Point(bottomLeft.x, half + 1)
        return countShips(sea, midTopRight, bottomLeft) + countShips(sea, topRight, midBottomLeft)

ships = [[1,1],[2,2],[3,3],[5,5]]
topRight = [4,4]
bottomLeft = [0,0]
sea = Sea(topRight, bottomLeft)
countShips(sea, topRight, bottomLeft)