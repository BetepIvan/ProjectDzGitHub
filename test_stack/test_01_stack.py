import unittest

from stack_app.stack_04_OOP_stack_node import Node, Stack


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node_1 = Node(5)
        self.node_2 = Node(3, self.node_1)

    def test_01_node(self):
        self.assertEqual(self.node_1.data, 5)
        self.assertEqual(self.node_1.next_node, None)
        self.assertEqual(self.node_2.data, 3)
        self.assertEqual(self.node_2.next_node, self.node_1)
        self.assertEqual(self.node_2.next_node.data, 5)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    # не обязательно, т.к. тестируется из методов
    # def test_02_init(self):
    #     self.assertEqual(self.stack.top, None)

    def test_03_push(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.top.data, 'test_data')

    def test_04_pop(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.pop(), 'test_data')
        self.assertEqual(self.stack.top, None)