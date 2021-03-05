from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        n=0
        if ruleKey == "type":
            for item in items:
                if item[0] == ruleValue:
                    n+=1
        elif ruleKey == "color":
            for item in items:
                if item[1] == ruleValue:
                    n+=1
        else:
            for item in items:
                if item[2] == ruleValue:
                    n+=1
        return n