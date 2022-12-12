from collections import deque
from string import ascii_lowercase
from typing import Dict, List, Set


letter_to_value = {c: i for i, c in enumerate(ascii_lowercase)}
letter_to_value['S'] = letter_to_value['a']
letter_to_value['E'] = letter_to_value['z']


class Node:

    def __init__(self, i, j, letter):
        self.i = i
        self.j = j
        self.letter = letter
        self.value = letter_to_value[letter]

    def __repr__(self):
        return f'{self.letter}({self.i}, {self.j})'

    def __str__(self):
        return f'{self.letter}({self.i}, {self.j})'

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __hash__(self):
        return hash(self.__str__())


class DirectedEdge:

    def __init__(self, v: Node, w: Node):
        self.v = v
        self.w = w

    def source(self) -> Node:
        return self.v

    def to(self) -> Node:
        return self.w

    def __str__(self):
        return f'{self.v} -> {self.w}'

    def __repr__(self):
        return f'{self.v} -> {self.w}'


class Digraph:

    def __init__(self, nr_vertices: int):
        self.V = nr_vertices
        self.E = 0
        self.adj: Dict[Node, List[Node]] = {}

    def nr_vertices(self) -> int:
        return self.V

    def nr_edges(self) -> int:
        return self.E

    def nodes(self) -> List[Node]:
        return self.adj.keys()

    def add_edge(self, e: DirectedEdge) -> None:
        if e.v in self.adj:
            self.adj[e.v].append(e.w)
        else:
            self.adj[e.v] = [e.w]
        self.E += 1

    def adjacent_edges(self, v: Node) -> List[Node]:
        return self.adj[v]

    def edges(self) -> List[DirectedEdge]:
        edges_list = []
        for v, w in self.adj.items():
            e = DirectedEdge(v, w)
            edges_list.append(e)
        return edges_list

    def __str__(self):
        s = f'V: {self.V}, E: {self.E}\n'
        for e in self.edges():
            s = f'{s}{e}\n'
        return s


def _is_valid(v: Node, w:Node) -> bool:
    if w is None:
        return False
    return w.value - v.value <= 1


def determine_edges(n: Node) -> List[DirectedEdge]:
    node_edges = []
    r, c = n.i, n.j
    possible = [
        nodes.get((r, c-1)),
        nodes.get((r, c+1)),
        nodes.get((r-1, c)),
        nodes.get((r+1, c))
    ]
    valid = [w for w in possible if _is_valid(n, w)]
    for w in valid:
        e = DirectedEdge(n, w)
        node_edges.append(e)
    return node_edges


class BreadFirstPaths:

    def __init__(self, g: Digraph, s: Node):
        self.g = g
        self.s = s

        # last vertex on known path to this vertex
        self.edge_to: Dict[Node, Node] = {}

        # is a SP to this vertex known?
        self.visited: Set[Node] = {s}
        self._bfs()

    def _bfs(self):
        queue = deque()
        queue.append(self.s)

        while len(queue) != 0:
            v = queue.pop()
            # print(v)
            for w in self.g.adjacent_edges(v):
                if w not in self.visited:
                    self.edge_to[w] = v
                    self.visited.add(w)
                    queue.appendleft(w)

    def has_path_to(self, v: Node):
        return v in self.visited

    def path_to(self, v: Node):
        if not self.has_path_to(v):
            return None

        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]
        return path


with open('../../days_inputs/day-12.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    print(f'read {len(lines)} lines')

    # set with all nodes seen while reading the file
    nodes = {}

    # variables with nodes of the 'source' and 'end' nodes
    source_node = None
    end_node = None

    # read all lines and create the graph nodes
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            node = Node(i, j, c)
            nodes[(i, j)] = node
            if c == 'S':
                source_node = node
            if c == 'E':
                end_node = node

    # initialize a graph structure
    graph = Digraph(len(nodes))

    # part 2
    starting_points = [source_node]

    # iterate over nodes, determine the valid edges for each node
    # and add each one of them to the graph
    for node in nodes.values():
        # add node edges
        if node.letter == 'a':
            starting_points.append(node)
        edges = determine_edges(node)
        for e in edges:
            graph.add_edge(e)

    print(graph)

    # part 1
    # run BFS on a digraph where the edges do not have weights
    g_bfs = BreadFirstPaths(graph, source_node)
    path = g_bfs.path_to(end_node)
    print(f'[part1] {len(path)}, path: {path}')

    # part 2
    min_steps = 1e20
    # iterate over the possible starting points and run BFS
    for sp in starting_points:
        g_bfs = BreadFirstPaths(graph, sp)
        path = g_bfs.path_to(end_node)
        if path is not None:
            min_steps = min(len(path), min_steps)

    print(f'[part2] min_steps: {min_steps}')
