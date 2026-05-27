class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i,n in enumerate(nums):
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        l=[]*k
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        # Step 3: Traverse buckets backwards
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
        
        

            
        