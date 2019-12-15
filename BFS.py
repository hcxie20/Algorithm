'''
page: 345 or 594(Eng)
'''


class Graph:
    def __init__(self, num):
        self.num = num
        self.nodes = []
        self.adj = []
        self.rst_bfs = []
        for i in range(num):
            tmp = self.LinkedList()
            tmp.node.value = i
            self.adj.append(tmp)
            self.nodes.append(self.Node(i))

    def bfs(self, src):
        '''
        s: start point, int
        '''
        node_list_tmp = self.nodes
        node_list_tmp[src].d = 0
        node_list_tmp[src].color = "GRAY"
        q = self.Queue()
        print("Node {0} found".format(src))
        q.enqueue(src)
        while q.is_empty() != 1:
            tmp = q.dequeue()
            print("Start to find node {0}'s adjacent".format(tmp))
            for node in self.adj[tmp].all():
                print("Foud node {0}, {1}".format(node, node_list_tmp[node].color))
                if node_list_tmp[node].color == "WHITE":
                    node_list_tmp[node].color = "GRAY"
                    node_list_tmp[node].d = node_list_tmp[tmp].d + 1
                    node_list_tmp[node].pre = tmp
                    q.enqueue(node)
            node_list_tmp[tmp].color = "BLACK" 
            print("Node {0} changed to BLACK".format(tmp))
        self.rst_bfs = node_list_tmp
    
    def print_path(self, src, dst):
        if src == dst:
            print(src)
        elif self.rst_bfs[dst].pre == None:
            print("No path")
        else:
            self.print_path(src, self.rst_bfs[dst].pre)
            print(dst)

    def add_edge(self, u, v):
        '''
        u: from
        v: to
        '''
        self.adj[u].append(v)

    class Node:
        def __init__(self, i):
            self.value = i
            self.color = "WHITE"
            self.pre = None
            self.d = float("inf")

    class LinkedList:
        def __init__(self):
            self.node = self.LinkedListNode()

        def append(self, value):
            tmp = self.node
            while tmp.next != None:
                tmp = tmp.next

            a = self.LinkedListNode()
            a.value = value
            tmp.next = a
            return self

        def all(self):
            '''
            return all nodes connected
            donot contain the first node, which is it self
            '''
            tmp = self.node.next
            rst = []
            while tmp != None:
                rst.append(tmp.value)
                tmp = tmp.next

            return rst

        class LinkedListNode:
            def __init__(self):
                self.value = None
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
    a = Graph(8)
    a.add_edge(0, 1)
    a.add_edge(0, 3)
    a.add_edge(1, 0)
    a.add_edge(1, 2)
    a.add_edge(2, 1)
    a.add_edge(3, 1)
    a.add_edge(3, 4)
    a.add_edge(3, 7)
    a.add_edge(4, 3)
    a.add_edge(4, 5)
    a.add_edge(4, 6)
    a.add_edge(4, 7)
    a.add_edge(5, 4)
    a.add_edge(5, 6)
    a.add_edge(6, 4)
    a.add_edge(6, 5)
    a.add_edge(6, 7)
    a.add_edge(7, 3)
    a.add_edge(7, 4)
    a.add_edge(7, 6)

    a.bfs(0)
    a.print_path(0, 6)
    pass
