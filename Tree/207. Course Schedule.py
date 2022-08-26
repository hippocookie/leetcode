from typing import List


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

class Node:
    def __init__(self, value):
        self.out_degree = 0
        self.in_degree = 0
        self.value = value
        self.next = []
        self.edges = []

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    def __str__(self):
        return '[' + self.from_node.value + ',' + self.to_node.value + ']'


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        graph = self.createGraph(prerequisites)
        no_in_degree_queue = []
        learned = []

        for i in range(numCourses):
            for node in graph.nodes.values():
                if node.in_degree == 0 and node.value not in learned:
                    no_in_degree_queue.append(node)
                    learned.append(node.value)
            while no_in_degree_queue:
                node = no_in_degree_queue.pop()
                for next_node in node.next:
                    next_node.in_degree -= 1
        for i in range(numCourses):
            if i not in learned:
                return False
        return True

    def createGraph(self, prerequisites):
        graph = Graph()
        for item in prerequisites:
            if item[0] not in graph.nodes:
                graph.nodes[item[0]] = Node(item[0])
            if item[1] not in graph.nodes:
                graph.nodes[item[1]] = Node(item[1])
            from_node = graph.nodes[item[1]]
            to_node = graph.nodes[item[0]]
            edge = Edge(0, from_node, to_node)
            from_node.out_degree += 1
            to_node.in_degree += 1
            from_node.edges.append(edge)
            from_node.next.append(to_node)
            graph.edges.append(edge)
        return graph


if __name__ == '__main__':
    print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
