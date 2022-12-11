import copy

def get_test_data():
    inss = \
    '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''
    return inss


def get_data_1():
    ins = \
    '''addx 2
addx 3
addx -2
addx 3
noop
addx 6
addx -1
addx 4
addx 1
noop
addx 3
addx 1
addx 7
noop
noop
addx -1
addx 3
addx 2
noop
addx 4
addx 2
addx -25
addx -7
addx -4
addx 2
addx 2
addx 19
addx -8
addx -5
addx 2
addx -9
addx 16
addx 3
addx -2
addx 12
addx -5
addx 2
addx -15
noop
noop
noop
addx 5
addx 16
addx -22
addx -14
addx 5
noop
addx 29
noop
noop
noop
addx -21
addx 2
noop
noop
addx 5
addx -1
addx 1
noop
noop
addx 8
addx -2
addx 4
noop
addx -22
addx 29
noop
addx -36
noop
addx -2
addx 6
addx -2
addx 2
noop
noop
noop
addx 8
addx 2
addx 10
noop
addx -5
addx 3
addx -2
addx 9
addx -2
addx 2
addx -21
addx 10
addx 17
addx -38
noop
noop
noop
addx 34
addx -27
addx 2
addx -6
addx 7
addx 5
addx 2
addx 5
noop
noop
noop
addx 3
addx -2
addx 2
addx 5
addx 2
addx -29
addx 35
addx -3
addx -25
addx -8
addx 1
noop
addx 4
addx 3
addx -2
addx 5
noop
addx 8
addx -6
noop
addx -3
addx 10
noop
noop
addx 6
addx -1
addx -18
addx 21
addx -30
addx 37
addx 1
noop
noop
noop
noop'''
    return ins

def get_value_at_cycle(inss, initial_register_value, cycle):
    current_cycle = 1
    current_register = initial_register_value

    temp_var = 0
    for ins in inss:
        if ins == 'noop':
            current_cycle += 1
            # print(f'{ins} - cycle={current_cycle} - register={current_register}')
            if current_cycle == cycle:
                return current_register
        elif ins.split(' ')[0] == 'addx':
            value = int(ins.split(' ')[1])
            # operation
            temp_var = current_register + value
            current_cycle += 1
            # print(f'{ins} - cycle={current_cycle} - register={current_register}')
            if current_cycle == cycle:
                return current_register

            # sets registers
            current_register = temp_var
            current_cycle += 1
            # print(f'{ins} - cycle={current_cycle} - register={current_register}')
            if current_cycle == cycle:
                return current_register


def draws(inss, initial_register_value):
    current_cycle = 0
    current_register = initial_register_value

    temp_var = 0
    rows = []
    current_row = []
    register_values = []

    for ins in inss:
        current_cycle += 1

        if ins == 'noop':
            if (current_cycle % 40) in [current_register, current_register+1, current_register+2]:
                current_row.append('#')
            else:
                current_row.append('.')
                # print(f"{ins} - cycle={current_cycle} - register_value={current_register}")
                # print(current_row)

        elif ins.split(' ')[0] == 'addx':
            value = int(ins.split(' ')[1])
            # operation
            temp_var = current_register + value
            if (current_cycle % 40) in [current_register, current_register+1, current_register+2]:
                current_row.append('#')
            else:
                current_row.append('.')
            # print(f"{ins} - cycle={current_cycle} - register_value={current_register}")
            # print(current_row)
            if (current_cycle % 40) == 0:
                # print(current_row)
                rows.append(copy.copy(current_row))
                current_row = []

            # sets registers
            current_cycle += 1
            if (current_cycle % 40) in [current_register, current_register+1, current_register+2]:
                current_row.append('#')
            else:
                current_row.append('.')
            current_register = temp_var
            register_values.append(current_register)
            # print(f"{ins} - cycle={current_cycle} - register_value={current_register}")
            # print(current_row)

        if (current_cycle % 40) == 0:
            # print(current_row)
            rows.append(copy.copy(current_row))
            current_row = []

    rows.append(copy.copy(current_row))
    print(register_values)
    return rows

def prob1():
    inss = [d for d in get_data_1().split('\n')]
    initial_register_value = 1

    register_values = []
    strengths = []
    for cycle in [20, 60, 100, 140, 180, 220]:
        register_value = get_value_at_cycle(inss, initial_register_value, cycle)
        register_values.append(register_value)
        strength = register_value*cycle
        strengths.append(strength)
        print(f'cycle {cycle} = register_value={register_value}, strength={strength}')
    print(f'sum strengths={sum(strengths)}')

def prob2():
    inss = [d for d in get_data_1().split('\n')]
    initial_register_value = 1
    drawings = draws(inss, initial_register_value)
    for r in drawings:
        print(f'{"".join(r)}')

if __name__ == '__main__':
    prob2()
