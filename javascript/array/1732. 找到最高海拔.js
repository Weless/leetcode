var largestAltitude = function(gain) {
    res = [0]
    for(let i=0;i<gain.length;i++){
        res[i+1] = res[i] + gain[i]
    }
    return Math.max(...res)
};

