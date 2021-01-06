class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        i,j =0, l//2
        ci,cj=0,0
        while j<l:
            if s[i].upper() in ['A','E','I','O','U']:
                ci+=1
            if s[j].upper() in ['A','E','I','O','U']:
                cj+=1
            i+=1
            j+=1
        return ci == cj
