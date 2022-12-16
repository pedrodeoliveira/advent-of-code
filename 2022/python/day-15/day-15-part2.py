import re
import time
from dataclasses import dataclass
# from __future__ import annotations

from typing import Set


@dataclass
class Point:

    x: int
    y: int
    type: str

    @classmethod
    def build_sensor(cls, i: int, j: int):
        return cls(i, j, 'S')

    @classmethod
    def build_beacon(cls, i: int, j: int):
        return cls(i, j, 'B')

    def distance(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def bounds(self, other, y_target: int) -> (int, int):
        d = self.distance(other)
        aux = d - abs(self.y - y_target)
        lower = self.x - aux
        upper = self.x + aux
        return lower, upper

    def bounds_y(self, other):
        d = self.distance(other)
        return [self.y-d, self.y+d]

    def bounds_x(self, other):
        d = self.distance(other)
        return [self.x-d, self.x+d]

    def in_bounds_y(self, other, y_target: int):
        lower, upper = self.bounds_y(other)
        return lower <= y_target <= upper

    def bounds_y_set(self, other):
        lower, upper = self.bounds_y(other)
        y_set = set([i for i in range(lower, upper + 1)])
        return y_set

    def is_point_out_perimeter(self):
        dist_p_to_s = [self.distance(s) for s, _ in sensors.items()]
        diffs = [dist_p_to_s[i] - dist_s_to_b[i] for i in range(len(dist_p_to_s))]
        for i in range(len(dist_p_to_s)):
            if diffs[i] < 1:
                return False
        return True

    def get_points_in_perimeter(self, other, lower_bound, upper_bound):
        d = self.distance(other) + 1
        points = set()
        for i in range(d+1):
            x_lo = max(self.x - d + i, lower_bound)
            x_hi = min(self.x + d - i, upper_bound)
            y_hi = min(self.y + i, upper_bound)
            y_lo = max(self.y - i, lower_bound)
            p1 = Point(x_lo, y_hi, '#')
            p2 = Point(x_lo, y_lo, '#')
            p3 = Point(x_hi, y_hi, '#')
            p4 = Point(x_hi, y_lo, '#')
            points.update([p1, p2, p3, p4])
        return points

    def bounds_set(self, other, y_target, x_min, x_max) -> Set[int]:
        lower, upper = self.bounds(other, y_target)
        lower = max(x_min, lower)
        upper = min(x_max, upper)
        b_set = set([i for i in range(lower, upper+1)])
        if other.x in b_set and other.y == y_target:
            b_set.remove(other.x)
        return b_set

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x},{self.y},{self.type})'

    def __str__(self):
        return f'({self.x},{self.y},{self.type})'

    def __hash__(self):
        return hash(f'({self.x}, {self.y})')


with open('../../days_inputs/day-15.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    print(f'read {len(lines)} lines')

    sensors = {}
    beacons = set()

    up_bound = 4e6
    dw_bound = 0

    sensors_perimeters = {}
    for i, line in enumerate(lines):
        # st = time.time()
        coordinates = re.findall(r'-?[0-9]\d*', line)
        # print(coordinates)
        s = Point.build_sensor(int(coordinates[0]), int(coordinates[1]))
        b = Point.build_beacon(int(coordinates[2]), int(coordinates[3]))
        sensors[s] = b
        beacons.add(b)
        print(f's={s} with d={s.distance(b):2d}, x in {s.bounds_x(b)}, '
              f'y in {s.bounds_y(b)}')

        pts = s.get_points_in_perimeter(b, dw_bound, up_bound)
        sensors_perimeters[s] = pts
        # print(f's={s} with points={pts}')
        # print(f'{(time.time() - st):.1f}s')

    dist_s_to_b = [s.distance(b) for s, b in sensors.items()]

    for s, pts in sensors_perimeters.items():
        print(f'checking pts for sensor {s}')
        for p in pts:
            if p.is_point_out_perimeter():
                print(f'Found point outside perimeter at {p}')
                break
        else:
            continue
        break

    # min_x = -2
    # max_x = 25
    # min_y = 0
    # max_y = 22
    #
    # test_point = Point(14, 11, '#')
    # print(test_point.is_point_out_perimeter())

    # for s, pts in sensors_perimeters.items():
    #     print(f'Perimeter points for s {s}')
    #     for y in range(min_y, max_y+1):
    #         for x in range(min_x, max_x+1):
    #             p = Point(x, y, '.')
    #             if p in sensors:
    #                 print('S', end='')
    #             elif p in beacons:
    #                 print('B', end='')
    #             elif p in pts:
    #                 print('#', end='')
    #             else:
    #                 print('.', end='')
    #         print()

    # total_y_set = set()
    # for s, b in sensors.items():
    #     sensor_y_set = s.bounds_y_set(b)
    #     total_y_set.update(sensor_y_set)
    # print(len(total_y_set))

    # print(f'row bounds with len {len(row_bounds)}. {row_bounds}')
    # print(f'row bounds with len {len(row_bounds)}')

    # x_limit = 20
    #
    # all_possible_x = set([i for i in range(0, x_limit+1)])
    #
    # for y_target in range(0, x_limit+1):
    #     if y_target % 1000 == 0:
    #         print(y_target)
    #     row_bounds = set()
    #     for s, b in sensors.items():
    #         sensor_bounds = s.bounds_set(b, y_target, 0, x_limit)
    #         if s.y == y_target:
    #             sensor_bounds.add(s.x)
    #         if b.y == y_target:
    #             sensor_bounds.add(b.x)
    #         row_bounds.update(sensor_bounds)
    #
    #     diff = all_possible_x.difference(row_bounds)
    #     if len(diff) != 0:
    #         x = diff.pop()
    #         frequency = x + x_limit + y
    #         print(f'x: {x}, y: {y_target}')
    #         print(f'tuning frequency: {frequency}')
