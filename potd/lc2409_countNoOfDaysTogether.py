class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        datesOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        prefixSum=[0]

        for date in datesOfMonths : 
            prefixSum.append(prefixSum[-1]+date)
        
        def calculateDayOfYear(day : str , prefixSum : list ) :
            month=int(day[:2])
            date=int(day[3:])

            return prefixSum[month-1] + date 
        
        a1=calculateDayOfYear(arriveAlice,prefixSum)
        a2=calculateDayOfYear(leaveAlice,prefixSum)
        b1=calculateDayOfYear(arriveBob,prefixSum)
        b2=calculateDayOfYear(leaveBob,prefixSum)

        return max(0,min(a2,b2)-max(a1,b1)+1)