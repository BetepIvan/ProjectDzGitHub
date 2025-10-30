from stack_app.stack_04_OOP_stack_node import Stack
from stack_app.stack_04_OOP_stack_node_adv import Stack as StackInt


if __name__ == '__main__':
    # node_1 = Node('2 RUB')
    # node_2 = Node('5 RUB', node_1)
    # node_3 = Node('10 RUB', node_2)
    # print(node_1.data)
    # print(node_2.data)
    # print(node_3.next_node.next_node.data)
    # #             >> node2  >> node1

    stack1 = Stack()
    stack1.push('2 RUB')
    stack1.push('5 RUB')
    stack1.push('10 RUB')

    # print(stack.top.data)
    # print(stack.top.next_node.data)
    # print(stack.top.next_node.next_node.data)

    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())

    for i in range(10):
        try:
            print(f'{stack1.pop()}')
        except AttributeError:
            print('Stack is Empty')
            break
    print('Data extracted')

    stack2 = StackInt(4)
    stack2.push(1)
    stack2.push('str')
    stack2.push(3)
    stack2.push(0.5)
    stack2.push('str2')
    print(StackInt.counter_int(stack2))

    # просто для примера объект другого класса
    print(StackInt.counter_int(stack1))