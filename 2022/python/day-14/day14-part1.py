

class TreeNode:
    def __init__(self, value, marker):
        self.value = value
        self.marker = marker

    def is_rock(self) -> bool:
        return self.marker == '#'

    def is_sand(self) -> bool:
        return self.marker == 'o'

    def is_free(self) -> bool:
        return self.marker == '.'

    def mark_with_sand(self):
        tree_nodes[self.value].marker = 'o'

    def left(self):
        idx = self._left_idx()
        return self._get_tree_node(idx)

    def right(self):
        idx = self._right_idx()
        return self._get_tree_node(idx)

    def center(self):
        idx = self._center_idx()
        return self._get_tree_node(idx)

    @staticmethod
    def _get_tree_node(idx):
        return tree_nodes[idx]

    def _left_idx(self):
        i, j = self.value
        return i-1, j+1

    def _right_idx(self):
        i, j = self.value
        return i+1, j+1

    def _center_idx(self):
        i, j = self.value
        return i, j+1

    def has_left(self) -> bool:
        idx = self._left_idx()
        return self._is_idx_free(idx)

    def has_center(self) -> bool:
        idx = self._center_idx()
        return self._is_idx_free(idx)

    @staticmethod
    def _is_idx_free(idx):
        if idx in tree_nodes:
            return tree_nodes[idx].is_free()
        return False

    def has_right(self) -> bool:
        idx = self._right_idx()
        return self._is_idx_free(idx)

    def __repr__(self):
        return f'[{self.value}]'

    def __str__(self):
        return f'[{self.value}]'

    def traverse(self):
        node = self
        if node.has_center():
            return to_be_named(node.center())
        return False


def to_be_named(node: TreeNode):
    if node.has_center():
        return to_be_named(node.center())
    elif node.has_left():
        return to_be_named(node.left())
    elif node.has_right():
        return to_be_named(node.right())
    node.mark_with_sand()
    # print(f'sand at {node}')
    if node.value[0] == global_min_x or node.value[0] == global_max_x:
        return False
    return True


def build_tree_nodes():
    for j in range(0, global_max_y + 1):
        for i in range(global_min_x, global_max_x + 1):
            e = i, j
            if e in tree_nodes:
                continue
            if e in rocks:
                n = TreeNode(e, '#')
            else:
                n = TreeNode(e, '.')
            tree_nodes[e] = n


def print_grid():
    for j in range(0, global_max_y + 1):
        for i in range(global_min_x, global_max_x + 1):
            e = i, j
            if e in tree_nodes:
                print(tree_nodes[e].marker, end='')
            elif e in rocks:
                print('#', end='')
            else:
                print('.', end='')
        print()


with open('../../days_inputs/day-14.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    # print(f'read {len(lines)} lines')

    rocks = set()
    global_min_x = 1e12
    global_max_x = -1
    global_min_y = 1e12
    global_max_y = -1

    for line in lines:
        rocks_str = line.split(' -> ')
        previous = None
        for rock in rocks_str:
            curr = tuple([int(s) for s in rock.split(',')])

            global_min_x = min(global_min_x, curr[0])
            global_max_x = max(global_max_x, curr[0])
            global_min_y = min(global_min_y, curr[1])
            global_max_y = max(global_max_y, curr[1])

            if previous is not None:
                if curr[0] == previous[0]:
                    diff = curr[0] - previous[0]
                    min_y = min(previous[1], curr[1])
                    max_y = max(previous[1], curr[1])
                    print(f'add V rocks between {min_y} and {max_y} at x={curr[0]}')
                    for i in range(min_y+1, max_y):
                        r = curr[0], i
                        print(f'adding rock {r}')
                        rocks.add(r)
                else:
                    diff = curr[1] - previous[1]
                    min_x = min(previous[0], curr[0])
                    max_x = max(previous[0], curr[0])
                    print(f'add H rocks between {min_x} and {max_x} at y={curr[1]}')
                    for i in range(min_x+1, max_x):
                        r = i, curr[1]
                        print(f'adding rock {r}')
                        rocks.add(r)

            previous = curr
            rocks.add(curr)

    print(f'global (min,max) -> x: ({global_min_x}, {global_max_x}), '
          f'y: ({global_min_y}, {global_max_y})')
    print(rocks)

    # build the tree
    root = TreeNode((500, 0), '+')
    tree_nodes = {(500, 0): root}
    print_grid()
    build_tree_nodes()
    # print()
    # print_grid()

    k = 0
    while root.traverse():
        if k % 1000 == 0:
            print(f'k: {k}')
            print_grid()
        k += 1
    print('terminated')
    print(f'k: {k}')
    # result: 885
    print_grid()

