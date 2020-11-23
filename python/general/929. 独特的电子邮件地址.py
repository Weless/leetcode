class Solution:
    def numUniqueEmails(self, emails):
        result = set()
        for email in emails:
            localName, domain = email.split("@")
            localName = localName.replace('.','')
            index = len(localName)
            if '+' in localName:
                index = localName.index('+')
            localName = localName[:index]
            result.add(localName+"@"+domain)
        return len(result)

s = Solution()
inputList = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
inputList2 = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(s.numUniqueEmails(inputList2))


''' other answer


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local_name,domain_name = email.split("@")
            local_name ="".join(local_name.split('+')[0].split('.')) // 简洁
            email = local_name +'@' + domain_name
            email_set.add(email)
        return len(email_set)

'''