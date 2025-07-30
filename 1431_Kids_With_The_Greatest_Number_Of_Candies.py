class Solution:
    from typing import List
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maxcandies=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxcandies:
                result+=[True]
            else:
                result+=[False]
        return result    