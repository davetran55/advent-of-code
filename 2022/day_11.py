import copy


def get_test_data():
    monkeys =[
        {'items': [79, 98], 'ops': lambda old: old*19, 'test_value': 23, 'true_throw_to': 2, 'false_throw_to': 3, 'inspected': []},
        {'items': [54, 65, 75, 74], 'ops': lambda old: old +6, 'test_value': 19, 'true_throw_to': 2, 'false_throw_to': 0, 'inspected': []},
        {'items': [79, 60, 97], 'ops': lambda old: old * old, 'test_value': 13, 'true_throw_to': 1,
         'false_throw_to': 3, 'inspected': []},
        {'items': [74], 'ops': lambda old: old + 3, 'test_value': 17, 'true_throw_to': 0,
         'false_throw_to': 1, 'inspected': []},
    ]
    return monkeys

def get_data1():
    monkeys =[
        {'items': [98, 70, 75, 80, 84, 89, 55, 98], 'ops': lambda old: old*2, 'test_value': 11, 'true_throw_to': 1, 'false_throw_to': 4, 'inspected': []},

        {'items': [59], 'ops': lambda old: old * old, 'test_value': 19, 'true_throw_to': 7, 'false_throw_to': 3, 'inspected': []},

        {'items': [77, 95, 54, 65, 89], 'ops': lambda old: old + 6, 'test_value': 7, 'true_throw_to': 0,
         'false_throw_to': 5, 'inspected': []},

        {'items': [71, 64, 75], 'ops': lambda old: old + 2, 'test_value': 17, 'true_throw_to': 6,
         'false_throw_to': 2, 'inspected': []},

        {'items': [74, 55, 87, 98], 'ops': lambda old: old * 11, 'test_value': 3, 'true_throw_to': 1,
         'false_throw_to': 7, 'inspected': []},

        {'items': [90, 98, 85, 52, 91, 60], 'ops': lambda old: old + 7, 'test_value': 5, 'true_throw_to': 0,
         'false_throw_to': 4, 'inspected': []},

        {'items': [99, 51], 'ops': lambda old: old + 1, 'test_value': 13, 'true_throw_to': 5,
         'false_throw_to': 2, 'inspected': []},

        {'items': [98, 94, 59, 76, 51, 65, 75], 'ops': lambda old: old + 5, 'test_value': 2, 'true_throw_to': 3,
         'false_throw_to': 6, 'inspected': []},
    ]
    return monkeys

def max_eq(x):
    new_x = x * 19
    new_x += 6
    new_x *= new_x
    new_x += 3
    return new_x

def prob1():
    monkeys = get_data1()
    # max_value = 23 * 19 * 13 * 17
    max_value = max_value = 11 * 19 * 7 * 17 * 3 * 5 * 13 * 2
    for i in range(10000):
        for mi in range(len(monkeys)):
            monkey = monkeys[mi]
            items = monkey.get('items')
            for item in items:
                new_value = monkey.get('ops')(item)
                # new_value = int(new_value / 3)
                new_value = new_value % max_value
                if (new_value % monkey.get('test_value')) == 0:
                    monkey_index = monkey.get('true_throw_to')
                else:
                    monkey_index = monkey.get('false_throw_to')
                monkeys[monkey_index].get('items').append(new_value)
                monkey.get('inspected').append(item)
            monkey.update({'items':[]})

    inspections = []
    for mi in range(len(monkeys)):
        monkey = monkeys[mi]
        # print(f'monkey {mi} inspected - {len(monkey.get("inspected"))}, holding - {monkey.get("items")}, inspected - {monkey.get("inspected")}')
        inspections.append(len(monkey.get("inspected")))
    inspections = sorted(inspections)
    print(f'{inspections[-2] * inspections[-1]} - {inspections}')



if __name__ == '__main__':
    prob1()
