class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        c=0
        while y>x:
            if y%2==0: y//=2;c+=1
            else: y+=1;c+=1
        return c+x-y
