function hide(e,reflow){
    if (reflow){
        e.style.display = "none";  // 隐藏这个元素，其所占的空间也随之消失
    }else{
        e.style.visibility="hidden";  // 将e隐藏，但是保留其所占的空间
    }
}

// 通过设置CSS类来高亮显示e
function hightlight(e){
    if(!e.className) e.className = "hilite";
    else e.className += " hilite"
}

