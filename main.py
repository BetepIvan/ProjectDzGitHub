def main():
    print('=== MASTER BRANCH VERSION ===')

    # Тестируем базовый стек
    stack1 = Stack()
    stack1.push('MASTER_DATA_1')
    stack1.push('MASTER_DATA_2')

    print('Basic Stack Operations:')
    for i in range(3):
        try:
            data = stack1.pop()
            print(f'Popped: {data}')
        except:
            print('Stack empty (master)')
            break

    # Тестируем расширенный стек
    stack2 = StackInt(3)
    stack2.push(100)
    stack2.push(200)
    stack2.push('MASTER_STRING')

    print(f'Integer count: {StackInt.counter_int(stack2)}')
    print('Master branch completed successfully!')


if __name__ == '__main__':
    main()