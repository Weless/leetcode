class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        while cur:
            node = Node(cur.val,None,None)
            node.next = cur.next
            cur.next = node
            cur = node.next
        cur = head
        while cur:
            node = cur.next
            node.random = cur.random.next if cur.random else None
            cur = node.next
        cur = head
        newhead = cur.next
        while cur:
            node = cur.next
            cur.next = node.next
            cur = cur.next
            if cur:
                node.next = cur.next
            else:
                node.next = None
        return newhead