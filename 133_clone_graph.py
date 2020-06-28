'''
use a dict to save origin -> new
'''

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return []
        visited = {node: Node(node.val, [])}

        queue = [node]
        while queue:
            old_node = queue.pop(0)

            for neighbor in old_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    neighbor_copy = Node(neighbor.val, [])
                    visited[neighbor] = neighbor_copy
                visited[old_node].neighbors.append(visited[neighbor])

        return visited[node]
