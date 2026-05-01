class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        tank = 0
        for i in range(len(cost)):
            tank = tank-cost[i]+gas[i]
            total = total-cost[i]+gas[i]
            if tank < 0:
                start = i + 1
                tank = 0
                if start==len(cost):
                    return -1
        if total < 0:
            return -1
        return start
            
            