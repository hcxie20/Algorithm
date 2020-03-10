class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.volumn = 0
        self.ls = doubleLinkedList()
        self.dictionary = {}

    def get(self, key: int) -> int:
        if key in self.dictionary:
            tmpNode = self.dictionary[key]
            self.ls.moveToTail(tmpNode)
            return tmpNode.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            node = self.dictionary[key]
            node.val = value
            self.ls.moveToTail(node)
        else:
            if self.volumn == self.capacity:
                headNode = self.ls.getHead()
                self.dictionary.pop(headNode.key)
                self.ls.removeNode(headNode)
                node = Node(key, value)
                self.dictionary[key] = node
                self.ls.addNode(node)
            else:
                node = Node(key, value)
                self.dictionary[key] = node
                self.ls.addNode(node)
                self.volumn += 1

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class doubleLinkedList(object):
    def __init__(self):
        self.Anchor = Node(None, None)
        self.tail = self.Anchor

    def getHead(self):
        return self.Anchor.next

    def addNode(self, node):
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def removeNode(self, node):
        node.prev.next = node.next
        if node.next != None:
            # node is not tail
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.next = None

    def moveToTail(self, node):
        self.removeNode(node)
        self.addNode(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)