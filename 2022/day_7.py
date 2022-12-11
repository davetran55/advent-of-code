def adv_code():

    identifiers = {
        "a": "rock",
        "b": "paper",
        "c": "scissor",
        "x": "rock",
        "y": "paper",
        "z": "scissor",
    }
    shape_scores = {"rock": 1, "paper": 2, "scissor": 3}
    rules_score_dict = {
        "rock_rock": 3,
        "rock_paper": 0,
        "rock_scissor": 6,
        "paper_paper": 3,
        "paper_rock": 6,
        "paper_scissor": 0,
        "scissor_scissor": 3,
        "scissor_rock": 0,
        "scissor_paper": 6,
    }
    l_d_w_index_dict = {
        "x": 0,
        "y": 1,
        "z": 2,
    }
    l_d_w_list_dict = {
        "rock": ["scissor", "rock", "paper"],
        "paper": ["rock", "paper", "scissor"],
        "scissor": ["paper", "scissor", "rock"],
    }

    rules_score_dict_opp_first = {
        "rock_rock": 3,
        "rock_paper": 6,
        "rock_scissor": 0,
        "paper_paper": 3,
        "paper_rock": 0,
        "paper_scissor": 6,
        "scissor_scissor": 3,
        "scissor_rock": 6,
        "scissor_paper": 0,
    }
    total = 0
    input_file = "/Users/davetran/dev/kraken-core/data/adventofcode/2022/puzzle6_input.csv"
    with open(input_file, "r") as data_file:
        data = data_file.readlines()
    total = 0
    for line in data:
        line = line.strip()
        opp_shape = identifiers.get(line.split(" ")[0].lower())
        l_d_w = l_d_w_index_dict.get(line.split(" ")[1].lower())
        # your_shape = identifiers.get(line.split(" ")[1].lower())
        your_shape = l_d_w_list_dict.get(opp_shape)[l_d_w]
        your_score = rules_score_dict.get("_".join([your_shape, opp_shape])) + shape_scores.get(
            your_shape
        )
        print(your_score)
        total += your_score

    line = "C X"

    opp_shape = identifiers.get(line.split(" ")[0].lower())
    l_d_w = identifiers.get(line.split(" ")[1].lower())
    your_score = rules_score_dict.get("_".join([your_shape, opp_shape])) + shape_scores.get(
        your_shape
    )

    def find_intersection(lines):
        uniq_chars = set()
        for line in lines:
            for c in line:
                uniq_chars.add(c)

        intersection = ""
        for c in uniq_chars:
            if sum([1 if (line.find(c) > -1) else 0 for line in lines]) == 3:
                intersection = c
                break
        return intersection


def matrix_to_stacks(matrix):
    stacks = []
    count = 0
    for m in matrix:
        if count == 0:
            for mi in m:
                if mi.strip():
                    new_stack = []
                    new_stack.append(mi)
                    stacks.append(new_stack)
        else:
            for m_index in range(len(m)):
                if m[m_index].strip():
                    stacks[m_index].append(m[m_index])
        count += 1
    return stacks


def move(stacks, ins):
    for i in range(0, ins[0]):
        pi = stacks[ins[1] - 1].pop()
        stacks[ins[2] - 1].append(pi)


def move_2(stacks, ins):
    new_stack = []
    for i in range(0, ins[0]):
        pi = stacks[ins[1] - 1].pop()
        new_stack.insert(0, pi)
    stacks[ins[2] - 1].extend(new_stack)


def algo2(stack_data, stack_pos, inss):
    matrix = []
    for index in range(1, len(stack_data)):
        data = stack_data[index]
        data_p = [data[l] for l in stack_pos]
        matrix.append(data_p)

    stacks = matrix_to_stacks(matrix)
    for ins in inss:
        ins = [int(l) for l in ins.split(" ") if l.isnumeric()]
        move_2(stacks, ins)

    print(f"{[i[-1] for i in stacks ]}")

    ins = """$ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d
        $ cd a
        $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
        $ ls
        584 i
        $ cd ..
        $ cd ..
        $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k"""

def algo1(ins):
    root = {}
    cur_dir = root
    current_command = ""

    for line in ins.split("\n"):
        if line.startswith("$"):
            command_parts = line.split(" ")
            if command_parts[1] == "cd":
                if command_parts[2] == "/":
                    # cd into root
                    cur_dir = root
                elif command_parts[2] == ".":
                    # cd into current dir, do nothing
                    pass
                elif command_parts[2] == "..":
                    cur_dir = cur_dir.get("..")
                else:
                    # cd into a directory
                    new_cur_dir = cur_dir.get(command_parts[2])
                    cur_dir = new_cur_dir
            elif line.startswith("$ ls"):
                current_command = "ls"
        elif current_command == "ls":
            command_parts = line.split(" ")
            if command_parts[0] == "dir":
                cur_dir.update({command_parts[1]: {"..": cur_dir}})
            else:
                cur_dir.update({command_parts[1]: int(command_parts[0])})
    return root


def find_size(root, current_smallest):
    total_size = 0
    for r in root:
        if r != "..":
            v = root.get(r)
            if type(v) == dict:
                dir_size = find_size(v, current_smallest)
                # part 1 is slightly different here
                if dir_size >= 268565 and dir_size < current_smallest:
                    current_smallest = dir_size
                    print(f"{dir_size} - {r}")
                total_size += dir_size
            else:
                total_size += v
    return total_size