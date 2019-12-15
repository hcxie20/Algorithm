class Graph:
    def __init__(self, num):
        self.num = num
        self.nodes = []
        self.adj = []
        self.time = 0
        for i in range(num):
            tmp = self.LinkedList()
            tmp.node.value = i
            self.adj.append(tmp)
            self.nodes.append(self.Node(i))

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def dfs(self):
        self.time = 0
        for node in self.nodes:
            print("Start node {}, {}".format(node.value, node.color))
            if node.color == "WHITE":
                self.dfs_visit(node)

    def dfs_visit(self, node):
        self.time += 1
        node.color = "GRAY"
        print("Node {} is now {}".format(node.value, node.color))
        for node_num in self.adj[node.value].all():
            print("Found node {},  {}".format(self.nodes[node_num].value, self.nodes[node_num].color))
            if self.nodes[node_num].color == "WHITE":
                self.nodes[node_num].pre = node.value
                self.dfs_visit(self.nodes[node_num])
        self.time += 1
        node.color = "BLACK"
        node.f = self.time
        print("Node {} is now {}".format(node.value, node.color))

    def topological_sort(self):
        def sortf(node):
            return node.f

        self.dfs()
        tmp = self.nodes
        tmp.sort(key=sortf, reverse=True)
        for i in range(self.num):
            print(tmp[i].value)

    class Node:
        def __init__(self, i):
            self.value = i
            self.name = None
            self.color = "WHITE"
            self.pre = None
            self.d = float("inf")
            self.f = None

    class LinkedList:
        def __init__(self):
            self.node = self.LinkedListNode()

        def append(self, obj):
            tmp = self.node
            while tmp.next != None:
                tmp = tmp.next

            a = self.LinkedListNode()
            a.obj = obj
            tmp.next = a
            return self

        def all(self):
            tmp = self.node.next
            rst = []
            while tmp != None:
                rst.append(tmp.obj)
                tmp = tmp.next
            return rst

        class LinkedListNode:
            def __init__(self):
                self.obj = None
                self.next = None

    class Queue:
        def __init__(self):
            self.list = []
        
        def enqueue(self, obj):
            self.list.append(obj)

        def dequeue(self):
            return self.list.pop(0)

        def is_empty(self):
            return len(self.list) == 0


if __name__ == "__main__":
    a = Graph(6)
    a.add_edge(0, 1)
    a.add_edge(0, 3)
    a.add_edge(1, 4)
    a.add_edge(4, 3)
    a.add_edge(3, 1)
    a.add_edge(2, 4)
    a.add_edge(2, 5)
    a.add_edge(5, 5)

    a.dfs()

    # ---------------------------------------

    b = Graph(9)
    b.add_edge(0, 7)
    b.add_edge(0, 1)
    b.add_edge(1, 7)
    b.add_edge(1, 2)
    b.add_edge(2, 5)
    b.add_edge(3, 2)
    b.add_edge(3, 4)
    b.add_edge(4, 5)
    b.add_edge(6, 7)
    b.topological_sort()
