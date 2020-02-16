# implement a simple depth first search algorithm


class Node:
    count = 0
    visited = False

    def __init__(self):
        Node.count += 1
        self._id = Node.count
        self._nodes = set()
        print(self._id)

    def __repr__(self):
        return str(self._id)

    def __str__(self):
        return self.__repr__()

    @property
    def nodes(self):
        return self._nodes

    @property
    def id(self):
        return self._id

    def add_node(self):
        new_node = Node()
        self._nodes.add(new_node)
        print(f'Node {self._id} -> Node {new_node._id}')
        return new_node

    def connect_node(self, node):
        print(f'Node {self._id} -> Node {node._id}')
        self._nodes.add(node)


def count_sum_ids_under(node):
    sum = edges = 0
    for n in node:
        # if already visited, no need to calculate any further
        if not n.visited:
            n.visited = True
            sum += n.id
            print(f'return node id: {n.id}')

            if n.nodes:
                print(f'count_sum_ids_under({n.nodes})')
                inc_sum, edges_inc = count_sum_ids_under(n.nodes)
                edges += edges_inc
                edges += len(n.nodes)
                sum += inc_sum
    return sum, edges


nodes = [Node() for i in range(3)]
adjacency_matrix = [[1, 0, 1],
                    [0, 1, 1],
                    [1, 0, 0]]
for i, row in enumerate(adjacency_matrix):
    for j, val in enumerate(row):
        if val:
            nodes[i].connect_node(nodes[j])

print(count_sum_ids_under(nodes))

