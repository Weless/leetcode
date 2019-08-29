import Foundation

class Solution {
    func defangIPaddr(_ address: String) -> String {
        return address.replacingOccurrences(of: ".", with: "[.]")
    }
}

let s = Solution()

print(s.defangIPaddr("1.1.1.1"))


---other method---

class Solution{
    func defangIPaddr(_ address:String) -> String{
        let sequence = address.split(separator: ".")

        var result = ""
        sequence.enumerated().forEach{ (offset,element) in
            if offset != (sequence.endIndex - 1){
                result += element + "[.]"
            }else{
                result += element
            }
        }
        return result
    }
}
