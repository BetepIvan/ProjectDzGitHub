class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, top=None):
        self.top = top
        self.master_version = True  # Новая строка для конфликта

    def push(self, data):
        'Push method - MASTER VERSION'
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node
        return f'Pushed: {data} (master)'

    def pop(self):
        'Pop method - MASTER VERSION'
        if self.top is None:
            return 'Stack is empty (master)'
        remove_last = self.top
        self.top = self.top.next_node
        return remove_last.data

    def is_empty(self):
        'New method in master branch'
        return self.top is None