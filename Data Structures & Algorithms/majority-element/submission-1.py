class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        mp={}
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        return(max(mp, key=mp.get))


        '''
        
        return(max(Counter(nums)))'''
        