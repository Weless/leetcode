var tupleSameProduct = function(nums) {
    var d = {}
    for(var i=0;i<nums.length;i++){
        for (var j=i+1;j<nums.length;j++){
            var n = nums[i]*nums[j]
            d[n]? d[n]++ :d[n]=1
        }
    }
    var res = 0
    for (x in d){
        res += d[x] * (d[x]-1) / 2
    }
    return res * 8
};

console.log(tupleSameProduct([2,3,4,6]))