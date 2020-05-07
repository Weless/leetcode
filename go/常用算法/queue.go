package algorithem


// 初始化
var queue []int
var stack []int

// 入队 入栈
queue = append(queue, 1)
stack = append(stack, 1)

// 出队 出栈
queue = queue[1: len(queue)]
stack = stack[0: len(queue)-1]
