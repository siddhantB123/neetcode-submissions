class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## will car at lower position catch up and append itself to the car fleet 
        ## total number of distinct car fleets
        pair=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

        
        