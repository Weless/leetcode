class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

         res = []
         nums1 = list(reversed(num1))
         nums2 = list(reversed(num2))
         l1 = len(nums1)
         l2 = len(nums2)
         lmin = min(l1,l2)
         i = 0
         tag = 0
         while i < lmin:
             r = int(nums1[i]) + int(nums2[i]) + tag
             if r >= 10:
                 tag = 1
                 res.append(r-10)
             else:
                 tag = 0
                 res.append(r)
             i+=1
         if l1 == l2:
             pass
         elif l1 < l2:
             while i < l2:
                 r = int(nums2[i]) + tag
                 if r >= 10:
                     tag = 1
                     res.append(r-10)
                 else:
                     tag = 0
                     res.append(r)
                 i+=1
         else:
             while i< l1:
                 r = int(nums1[i]) + tag
                 if r >= 10:
                     tag = 1
                     res.append(r - 10)
                 else:
                     tag = 0
                     res.append(r)
                 i+=1
         if tag:
             res.append(1)
         return ''.join(map(str,reversed(res)))
s = Solution()
nums1 = "9133"
nums2 = "0"
print(s.addStrings(nums1,nums2))