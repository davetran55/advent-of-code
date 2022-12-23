import copy

def get_test_data():
    data = \
    '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''
    return data


def get_data():
    data = \
    '''abccccaaaaaaacccaaaaaaaccccccccccccccccccccccccccccccccccaaaa
abcccccaaaaaacccaaaaaaaaaaccccccccccccccccccccccccccccccaaaaa
abccaaaaaaaaccaaaaaaaaaaaaaccccccccccccccccccccccccccccaaaaaa
abccaaaaaaaaaaaaaaaaaaaaaaacccccccccaaaccccacccccccccccaaacaa
abaccaaaaaaaaaaaaaaaaaacacacccccccccaaacccaaaccccccccccccccaa
abaccccaaaaaaaaaaaaaaaacccccccccccccaaaaaaaaaccccccccccccccaa
abaccccaacccccccccaaaaaacccccccccccccaaaaaaaacccccccccccccccc
abcccccaaaacccccccaaaaaaccccccccijjjjjjaaaaaccccccaaccaaccccc
abccccccaaaaacccccaaaacccccccciiijjjjjjjjjkkkkkkccaaaaaaccccc
abcccccaaaaacccccccccccccccccciiiirrrjjjjjkkkkkkkkaaaaaaccccc
abcccccaaaaaccccccccccccccccciiiirrrrrrjjjkkkkkkkkkaaaaaccccc
abaaccacaaaaacccccccccccccccciiiqrrrrrrrrrrssssskkkkaaaaacccc
abaaaaacaaccccccccccccccccccciiiqqrtuurrrrrsssssskklaaaaacccc
abaaaaacccccccccccaaccccccccciiqqqttuuuurrssusssslllaaccccccc
abaaaaaccccccccaaaaccccccccciiiqqqttuuuuuuuuuuusslllaaccccccc
abaaaaaacccccccaaaaaaccccccciiiqqqttxxxuuuuuuuusslllccccccccc
abaaaaaaccccaaccaaaaacccccchhiiqqtttxxxxuyyyyvvsslllccccccccc
abaaacacccccaacaaaaaccccccchhhqqqqttxxxxxyyyyvvsslllccccccccc
abaaacccccccaaaaaaaacccccchhhqqqqtttxxxxxyyyvvssqlllccccccccc
abacccccaaaaaaaaaaccaaacchhhpqqqtttxxxxxyyyyvvqqqlllccccccccc
SbaaacaaaaaaaaaaaacaaaaahhhhppttttxxEzzzzyyvvvqqqqlllcccccccc
abaaaaaaacaaaaaacccaaaaahhhppptttxxxxxyyyyyyyvvqqqlllcccccccc
abaaaaaaccaaaaaaaccaaaaahhhppptttxxxxywyyyyyyvvvqqqmmcccccccc
abaaaaaaacaaaaaaacccaaaahhhpppsssxxwwwyyyyyyvvvvqqqmmmccccccc
abaaaaaaaaaaaaaaacccaacahhhpppssssssswyyywwvvvvvqqqmmmccccccc
abaaaaaaaacacaaaacccccccgggppppsssssswwywwwwvvvqqqqmmmccccccc
abcaaacaaaccccaaaccccccccgggppppppssswwwwwrrrrrqqqmmmmccccccc
abcaaacccccccccccccccccccgggggpppoosswwwwwrrrrrqqmmmmddcccccc
abccaacccccccccccccccccccccgggggoooosswwwrrrnnnmmmmmddddccccc
abccccccccccccccccccccccccccgggggooossrrrrrnnnnnmmmddddaccccc
abaccccaacccccccccccccccccccccgggfoossrrrrnnnnndddddddaaacccc
abaccaaaaaaccccccccccccccccccccgffooorrrrnnnneeddddddaaaacccc
abaccaaaaaacccccccccccccccccccccfffooooonnnneeeddddaaaacccccc
abacccaaaaaccccccccaaccaaaccccccffffoooonnneeeeccaaaaaacccccc
abcccaaaaacccccccccaaccaaaaccccccffffoooneeeeeaccccccaacccccc
abaccaaaaaccccccccaaaacaaaaccccccafffffeeeeeaaacccccccccccccc
abacccccccccccccccaaaacaaacccccccccffffeeeecccccccccccccccaac
abaaaacccccccaaaaaaaaaaaaaacccccccccfffeeeccccccccccccccccaaa
abaaaacccccccaaaaaaaaaaaaaaccccccccccccaacccccccccccccccccaaa
abaacccccccccaaaaaaaaaaaaaaccccccccccccaacccccccccccccccaaaaa
abaaaccccccccccaaaaaaaaccccccccccccccccccccccccccccccccaaaaaa'''
    return data


def steps1():
    data = get_test_data()
    all_data=[]
    S_coordinate = []
    for d in data.split():
        d_list = []
        for di in d:
            if di != 'S' and di != 'E':
                d_list.append(ord(di) - ord('a'))
            else:
                d_list.append(di)
        all_data.append(d_list)

    for ad in range(len(all_data)):
        print(all_data[ad])
        for adi in range(len(all_data[ad])):
            if all_data[ad][adi] == 'S':
                # print(f'S coordinate=[{ad},{adi}]')
                S_coordinate = [ad, adi]

    all_steps = []
    right_steps = [S_coordinate]
    down_steps = [S_coordinate]
    up_steps = [S_coordinate]
    # go right
    traverse([S_coordinate[0],S_coordinate[1]+1], all_data, right_steps, all_steps)
    # # go down
    # traverse([S_coordinate[0]-1,S_coordinate[1]], all_data, down_steps, all_steps)
    # # go up
    # traverse([S_coordinate[0]+1,S_coordinate[1]], all_data, up_steps, all_steps)

    print(f'length of right steps = {len(right_steps)-1}')
    print(f'length of down steps = {len(down_steps)-1}')
    print(f'length of up steps = {len(up_steps) - 1}')

    parts = data.split()
    print(data)
    for a_steps in all_steps:
        print(f'length={len(a_steps)-1}')
        print(''.join([parts[di[0]][di[1]] for di in a_steps]))
        print(a_steps)

def traverse(current, matrix, steps, all_steps):

    found = False

    # go up
    if not found and current[0] > 0:
        next_coordinate = [current[0]-1, current[1]]
        if matrix[current[0]][current[1]] == 25 and matrix[next_coordinate[0]][next_coordinate[1]] == 'E':
            all_steps.append(copy.copy(steps))
            print('up *****')
            return True
        if next_coordinate not in steps and matrix[next_coordinate[0]][next_coordinate[1]] != 'E':
            diff = matrix[next_coordinate[0]][next_coordinate[1]] - matrix[current[0]][current[1]]
            if diff in [0, 1]:
                print(f'up - current={current}, next_coordinate={next_coordinate}, steps={steps}')
                steps.append(current)
                found = traverse(next_coordinate, matrix, steps, all_steps)
                if not found:
                    steps.pop()

    # go left
    if not found and current[1] > 0:
        next_coordinate = [current[0], current[1]-1]
        if matrix[current[0]][current[1]] == 25 and matrix[next_coordinate[0]][next_coordinate[1]] == 'E':
            print('left *****')
            all_steps.append(copy.copy(steps))
            return True
        if next_coordinate not in steps and matrix[next_coordinate[0]][next_coordinate[1]] != 'E':
            diff = matrix[next_coordinate[0]][next_coordinate[1]] - matrix[current[0]][current[1]]
            if diff in [0, 1]:
                print(f'left - current={current}, next_coordinate={next_coordinate}, steps={steps}')
                steps.append(current)
                found = traverse(next_coordinate, matrix, steps, all_steps)
                if not found:
                    steps.pop()

    # go right
    if not found and current[1] < len(matrix[current[0]])-1:
        next_coordinate = [current[0], current[1] + 1]
        if matrix[current[0]][current[1]] == 25 and matrix[next_coordinate[0]][next_coordinate[1]] == 'E':
            print('right *****')
            all_steps.append(copy.copy(steps))
            return True
        if next_coordinate not in steps and matrix[next_coordinate[0]][next_coordinate[1]] != 'E':
            diff = matrix[next_coordinate[0]][next_coordinate[1]] - matrix[current[0]][current[1]]
            if diff in [0, 1]:
                print(f'right - current={current}, next_coordinate={next_coordinate}, steps={steps}')
                steps.append(current)
                found = traverse(next_coordinate, matrix, steps, all_steps)
                if not found:
                    steps.pop()

    # down
    if not found and current[0] < len(matrix)-1:
        next_coordinate = [current[0]+1, current[1]]
        if matrix[current[0]][current[1]] == 25 and matrix[next_coordinate[0]][next_coordinate[1]] == 'E':
            print('down *****')
            all_steps.append(copy.copy(steps))
            return True
        if next_coordinate not in steps and matrix[next_coordinate[0]][next_coordinate[1]] != 'E':
            diff = matrix[next_coordinate[0]][next_coordinate[1]] - matrix[current[0]][current[1]]
            if diff in [0, 1]:
                print(f'down - current={current}, next_coordinate={next_coordinate}, steps={steps}')
                steps.append(current)
                found = traverse(next_coordinate, matrix, steps, all_steps)
                if not found:
                    steps.pop()

    return found

if __name__ == '__main__':
    steps1()