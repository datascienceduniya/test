class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        r=n


        while True:
            mid=l+(r-l)//2

            mygues=guess(mid)

            if mygues==1:
                l=mid+1
            elif mygues==-1:
                r=mid-1

            else:
                return mid 