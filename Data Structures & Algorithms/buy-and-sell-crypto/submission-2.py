class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i+1
        max_p = 0

        while j<len(prices):
            val = prices[j]-prices[i]
            max_p = max(max_p,val)
            if(val<0):
                i=j
            j+=1
        
        return max_p
            