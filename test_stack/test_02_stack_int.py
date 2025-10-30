import unittest

from stack_app.stack_04_OOP_stack_node_adv import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(2)

    def test_05_push(self):
        self.stack.push('bottom_data')
        self.stack.push('top_data')
        self.assertEqual(self.stack.top.data, 'top_data')
        self.assertEqual(self.stack.top.next_node.data, 'bottom_data')
        self.assertEqual(self.stack.push('overflow_data'), None)
        self.assertEqual(self.stack.counter, 2)

    def test_06_pop(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.pop(), 'test_data')
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.counter, 0)

    def test_07_counter_int(self):
        self.stack.push(1)
        self.stack.push('top_data')
        self.assertEqual(Stack.counter_int(self.stack), 1)
        self.assertEqual(Stack.counter_int('wrong_class'), None)

    # данные метод отрабатывает в методе counter_int,
    # поэтому его отдельный тест не обязателен, но если надо:
    def test_08_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)