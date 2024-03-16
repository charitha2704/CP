class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        print(pairs)

        current_end=float('-inf')
        longest_chain=0

        for pair in pairs:
            if pair[0]>current_end:
                current_end=pair[1]
                longest_chain +=1

        return longest_chain
