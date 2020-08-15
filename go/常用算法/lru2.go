package algorithem

import "container/list"

type LRUCache struct {
	size     int
	capacity int
	cache    map[int]*list.Element
	ll       *list.List
}

type entry struct {
	key   int
	value int
}

func Constructor(capacity int) LRUCache {
	l := LRUCache{
		size:     0,
		capacity: capacity,
		cache:    make(map[int]*list.Element),
		ll:       list.New(),
	}
	return l
}

func (this *LRUCache) Get(key int) int {
	if ele, ok := this.cache[key]; ok {
		this.ll.MoveToFront(ele)
		return ele.Value.(*entry).value
	} else {
		return -1
	}
}

func (this *LRUCache) Put(key int, value int) {
	if ele, ok := this.cache[key]; ok {
		this.ll.MoveToFront(ele)
		ele.Value.(*entry).value = value
	} else {
		ele := this.ll.PushFront(&entry{key: key, value: value})
		this.cache[key] = ele
		this.size += 1
		if this.size > this.capacity {
			deleted := this.ll.Remove(this.ll.Back())
			delete(this.cache, deleted.(*entry).key)
			this.size -= 1
		}
	}
}
