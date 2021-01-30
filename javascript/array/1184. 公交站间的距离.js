
var distanceBetweenBusStops = function(distance, start, destination) {
    if (start > destination){
        let tmp = start
        start = destination
        destination = tmp
    }
    let total = 0;
    let res = 0;
    for (let i=0;i<distance.length;i++){
        total+=distance[i]
        if (i>=start && i<=destination-1){
            res+=distance[i]
        }
    }
    console.log(total,res)
    if (total-res > res){
        return res
    }
    return total - res
};