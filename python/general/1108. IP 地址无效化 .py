class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address = address.replace(".","[.]");
        return address

s = Solution()
print(s.defangIPaddr("1.1.1.1"));



#better result

'''
return '[.]'.join(address.split('.'))
'''

