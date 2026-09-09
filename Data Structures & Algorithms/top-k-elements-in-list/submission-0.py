from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        mp=Counter(nums)
        for _ in range(k):
            k=max(mp,key=mp.get)
            
            ans.append(k)
            del mp[k]
        return ans

        
        