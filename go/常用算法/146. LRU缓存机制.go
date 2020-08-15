package algorithem

type LRUCache struct {
	size     int
	capacity int
	cache    map[int]*DNode
	head     *DNode
	tail     *DNode
}

type DNode struct {
	key   int
	value int
	pre   *DNode
	next  *DNode
}

func initDNode(key, value int) *DNode {
	return &DNode{
		key:   key,
		value: value,
	}
}

func Constructor(capacity int) LRUCache {
	l := LRUCache{
		size:     0,
		capacity: capacity,
		cache:    make(map[int]*DNode),
		head:     initDNode(0, 0),
		tail:     initDNode(0, 0),
	}
	l.head.next = l.tail
	l.tail.pre = l.head
	return l
}

func (this *LRUCache) Get(key int) int {
	if _, ok := this.cache[key]; !ok {
		return -1
	}
	node := this.cache[key]
	this.moveToHead(node)
	return node.value
}

func (this *LRUCache) Put(key int, value int) {
	if _, ok := this.cache[key]; !ok {
		node := &DNode{key: key, value: value}
		this.cache[key] = node
		this.addToHead(node)
		this.size += 1
		if this.size > this.capacity {
			deleted := this.deleteTail()
			delete(this.cache, deleted.key)
			this.size -= 1
		}
	} else {
		node := this.cache[key]
		node.value = value
		this.moveToHead(node)
	}
}

func (this *LRUCache) deleteNode(node *DNode) {
	node.next.pre = node.pre
	node.pre.next = node.next
}

func (this *LRUCache) deleteTail() *DNode {
	node := this.tail.pre
	this.deleteNode(node)
	return node
}

func (this *LRUCache) moveToHead(node *DNode) {
	this.deleteNode(node)
	this.addToHead(node)
}

func (this *LRUCache) addToHead(node *DNode) {
	node.next = this.head.next
	this.head.next.pre = node
	node.pre = this.head
	this.head.next = node
}
