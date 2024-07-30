class Solution:
    def isPalindrome(self, s: str) -> bool:

        import re

        # string with letters, numbers, and special characters
        # s = "race a car"
        # keep only letters
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l=0
        r= len(s)-1


        while l < r:
            if s[l]==s[r]:
                l=l+1
                r=r-1
            else:
                return False
        return True


        