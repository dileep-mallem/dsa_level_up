import math
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find Closeset Point to the Rectngle and Dis <=radius

        if x1<= xCenter <= x2 :
            x=xCenter
        elif xCenter < x1 :
            x=x1
        elif xCenter > x2 :
            x=x2
        
        if y1<= yCenter <= y2 :
            y=yCenter
        elif yCenter < y1 :
            y=y1
        elif yCenter > y2 :
            y=y2

        dist = math.sqrt((x-xCenter)**2 + (y-yCenter)**2)

        return dist<=radius 
