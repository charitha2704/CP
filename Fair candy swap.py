class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        totalAlice=sum(aliceSizes)
        totalBob=sum(bobSizes)
        targetTotal=(totalAlice+totalBob)//2
        for aliceCandy in aliceSizes:
            bobCandy=aliceCandy+(targetTotal-totalAlice)
            if bobCandy in bobSizes:
                return[aliceCandy,bobCandy]
        
