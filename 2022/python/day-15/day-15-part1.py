import re
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

    def bounds_set(self, other, y_target) -> Set[int]:
        lower, upper = self.bounds(other, y_target)
        b_set = set([i for i in range(lower, upper+1)])
        if other.x in b_set and other.y == y_target:
            b_set.remove(other.x)
        return b_set

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.type == other.typer

    def __repr__(self):
        return f'({self.x},{self.y},{self.type})'

    def __str__(self):
        return f'({self.x},{self.y},{self.type})'

    def __hash__(self):
        return hash(self.__str__())


with open('../../days_inputs/day-15.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    print(f'read {len(lines)} lines')

    sensors = {}

    for line in lines:
        coordinates = re.findall(r'-?[0-9]\d*', line)
        # print(coordinates)
        s = Point.build_sensor(int(coordinates[0]), int(coordinates[1]))
        b = Point.build_beacon(int(coordinates[2]), int(coordinates[3]))
        sensors[s] = b

    y_target = 2000000
    row_bounds = set()
    for s, b in sensors.items():
        sensor_bounds = s.bounds_set(b, y_target)
        row_bounds.update(sensor_bounds)
        # print(f'sensor {s} has bounds: {sensor_bounds}')

    # print(f'row bounds with len {len(row_bounds)}. {row_bounds}')
    print(f'row bounds with len {len(row_bounds)}')

