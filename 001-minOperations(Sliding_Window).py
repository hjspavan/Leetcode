class Solution:
    def minOperations(self, a: list[int], x: int) -> int:
        k = sum(a) - x
        if k < 0 : return - 1
        best = -1

        s = i = 0

        for j, num in enumerate(a): 
            s += num 
            while s > k:
                s-=a[i]
                i+=1
            if s == k:
                best = max(best,j-i+1)
        return -1 if best < 0 else len (a) - best