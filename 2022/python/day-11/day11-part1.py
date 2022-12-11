import math
from collections import deque
import re


class Monkey:

    def __init__(self):
        self.list = deque()
        self.operation = ''
        self.operand = 0
        self.test_operand = 1
        self.throw_true = 0
        self.throw_false = 0
        self.nr_inspections = 0

    def parse_line(self, text):
        if text.lstrip().startswith('Starting'):
            items = [int(i) for i in re.findall(r'\d+', text)]
            self._initialize_item_list(items)
        elif text.lstrip().startswith('Operation'):
            self._set_operation(text)
        elif text.lstrip().startswith('Test'):
            self._set_test(text)
        else:
            monkey_nr = int(re.findall(r'\d+', text)[0])
            if text.lstrip().startswith('If true'):
                self._set_monkey_to_throw(monkey_nr, True)
            else:
                self._set_monkey_to_throw(monkey_nr, False)

    def process(self):
        throw_list = []
        while len(self.list) != 0:
            item = self.list.popleft()
            self.increment_inspections()
            worry_level = self._worry_level(item)
            worry_level /= 3
            worry_level = math.floor(worry_level)
            m_nr = self._get_monkey_to_throw(worry_level)
            throw_list.append((m_nr, worry_level))
        return throw_list

    def _initialize_item_list(self, items):
        for i in items:
            self.list.append(i)

    def _get_monkey_to_throw(self, worry_level):
        return self.throw_true if self._test(worry_level) else self.throw_false

    def _set_operation(self, text):
        operand = re.findall(r'\d+', text)
        if len(operand) == 0:
            self.operation = 'square'
        else:
            self.operation = '*' if '*' in text else '+'
            self.operand = int(operand[0])

    def _worry_level(self, item):
        if self.operation == '*':
            return item * self.operand
        elif self.operation == '+':
            return item + self.operand
        else:
            return item**2

    def _set_test(self, text):
        self.test_operand = int(re.findall(r'\d+', text)[0])

    def _set_monkey_to_throw(self, monkey_nr, result):
        if result:
            self.throw_true = monkey_nr
        else:
            self.throw_false = monkey_nr

    def receive_item(self, item):
        self.list.append(item)

    def _test(self, worry_level):
        return worry_level % self.test_operand == 0

    def increment_inspections(self):
        self.nr_inspections += 1

    def __str__(self):
        return f'items: {self.list}, operation: ({self.operation}, {self.operand}), ' \
               f'test: {self.test_operand}, throw: (' \
               f'{self.throw_true, self.throw_false}), ' \
               f'nr_inspections: {self.nr_inspections}'


with open('../../days_inputs/day-11.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    print(f'read {len(lines)} lines')

    level = 0
    nr_rounds = 20

    monkeys = []

    # read monkey notes
    for line in lines:
        if line == '':
            continue
        if line.startswith('Monkey'):
            m = Monkey()
            monkeys.append(m)
        else:
            m = monkeys[len(monkeys)-1]
            m.parse_line(line)

    # print monkeys notes
    for m in monkeys:
        print(m)

    for r in range(1, nr_rounds+1):
        print(f'[round {r:2d}]')
        for monkey_nr, monkey in enumerate(monkeys):
            # print(f'\tmonkey: {monkey_nr}')
            thrown_items = monkey.process()
            # print(f'\t\tthrown items: {thrown_items}')
            for monkey_to_rec, item in thrown_items:
                monkeys[monkey_to_rec].receive_item(item)

    inspections = [m.nr_inspections for m in monkeys]
    inspections.sort(reverse=True)
    print(inspections)
    level = inspections[0] * inspections[1]
    print(f'level: {level}')
