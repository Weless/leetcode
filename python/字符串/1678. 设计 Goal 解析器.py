class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        ans = ''
        while i<len(command):
            if command[i] == "G":
                ans+='G'
            else:
                tmp = ''
                while command[i] != ')':
                    tmp+=command[i]
                    i+=1
                tmp+=command[i]
                if tmp == "()":
                    ans+='o'
                if tmp == "(al)":
                    ans += "al"
            i+=1
        return ans