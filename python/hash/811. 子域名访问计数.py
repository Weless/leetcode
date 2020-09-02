from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = dict()
        for iterm in cpdomains:
            n,domain = iterm.split()
            if domain in d:
                d[domain] += int(n)
            else:
                d[domain] = int(n)
            s = domain.split('.')
            i = 1
            while i<len(s):
                tmp = ".".join(s[i:])
                if tmp in d:
                    d[tmp] += int(n)
                else:
                    d[tmp] = int(n)
                i+=1
        res = []
        for key,value in d.items():
            res.append(str(value) + " " + key)
        return res
s = Solution()
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(s.subdomainVisits(cpdomains))