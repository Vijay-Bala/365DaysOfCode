class Solution:
    def minOperations(self, n: int) -> int:
        return (n//2)**2 if n%2==0 else (n//2)*(n//2+1)
