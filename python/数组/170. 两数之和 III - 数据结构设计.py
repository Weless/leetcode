class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []
        self.isSorted = False

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.res.append(number)
        self.isSorted = False


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if not self.isSorted:
            self.res.sort()
            self.isSorted = True
        i,j = 0,len(self.res)-1
        while i<j:
            t = self.res[i] + self.res[j]
            if t == value:
                return True
            elif t < value:
                i+=1
            else:
                j-=1
        return False