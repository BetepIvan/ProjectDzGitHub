import copy


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, stack_size=5, top=None):
        self.top = top
        self.stack_size = stack_size
        self.counter = 0
        self.master_branch = True  # Новая строка

    def push(self, data):
        'Push method - MASTER BRANCH VERSION'
        if self.counter >= self.stack_size:
            print(f'MASTER: Stack overflow! Max: {self.stack_size}')
            return None

        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node
        self.counter += 1
        return f'MASTER: Pushed {data}'

    def pop(self):
        if self.is_empty():
            return 'MASTER: Stack is empty'
        remove_last = self.top
        self.top = self.top.next_node
        self.counter -= 1
        return remove_last.data

    @staticmethod
    def counter_int(stack):
        'Static method - MASTER VERSION'
        if not isinstance(stack, Stack):
            print('MASTER: Invalid stack object')
            return -1

        temp_stack = copy.deepcopy(stack)
        counter = 0
        while not temp_stack.is_empty():
            data = temp_stack.pop()
            if isinstance(data, int):
                counter += 1
        return counter

    def is_empty(self):
        return self.top is None

    def get_info(self):
        'New method only in master branch'
        return f'Master Stack: {self.counter}/{self.stack_size} items'