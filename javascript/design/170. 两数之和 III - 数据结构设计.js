/**
 * Initialize your data structure here.
 */
var TwoSum = function() {
    this.res = []
    this.isSorted = false
};

/**
 * Add the number to an internal data structure..
 * @param {number} number
 * @return {void}
 */
TwoSum.prototype.add = function(number) {
    this.res.push(number)
    this.isSorted = false
};

/**
 * Find if there exists any pair of numbers which sum is equal to the value.
 * @param {number} value
 * @return {boolean}
 */
TwoSum.prototype.find = function(value) {
    if(this.isSorted === false){
        this.res.sort(function (a,b){
            return a-b
        })
        this.isSorted = true
    }
    let i = 0
    let j = this.res.length -1
    while(i<j){
        let t = this.res[i] + this.res[j]
        if(t===value){
            return true
        }else if(t > value){
            j--
        }else{
            i++
        }
    }
    return false
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * var obj = new TwoSum()
 * obj.add(number)
 * var param_2 = obj.find(value)
 */