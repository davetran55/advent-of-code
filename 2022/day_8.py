def is_visible_left(x, y, col_height, row_len, matrix):
    vis_left = True
    for i in range(0, y):
        if matrix[x][y] <= matrix[x][i]:
            vis_left = False
            break
    return vis_left


def left_score(x, y, col_height, row_len, matrix):
    score = 0
    for i in range(y, 0, -1):
        score += 1
        if matrix[x][y] <= matrix[x][i - 1]:
            break
    return score


def is_visible_right(x, y, col_height, row_len, matrix):
    vis_right = True
    for i in range(y + 1, row_len):
        if matrix[x][y] <= matrix[x][i]:
            vis_right = False
            break
    return vis_right


def right_score(x, y, col_height, row_len, matrix):
    score = 0
    for i in range(y + 1, row_len):
        score += 1
        if matrix[x][y] <= matrix[x][i]:
            break
    return score


def is_visible_top(x, y, col_height, row_len, matrix):
    vis_top = True
    for i in range(x, 0, -1):
        if matrix[x][y] <= matrix[i - 1][y]:
            vis_top = False
            break
    return vis_top


def top_score(x, y, col_height, row_len, matrix):
    score = 0
    for i in range(x, 0, -1):
        score += 1
        if matrix[x][y] <= matrix[i - 1][y]:
            break
    return score


def is_visible_bottom(x, y, col_height, row_len, matrix):
    vis_bottom = True
    for i in range(x + 1, col_height):
        if matrix[x][y] <= matrix[i][y]:
            vis_bottom = False
            break
    return vis_bottom


def bottom_score(x, y, col_height, row_len, matrix):
    score = 0
    for i in range(x + 1, col_height):
        score += 1
        if matrix[x][y] <= matrix[i][y]:
            break
    return score


def total_score(i, ii, col_height, row_len, matrix):
    l = left_score(i, ii, col_height, row_len, matrix)
    r = right_score(i, ii, col_height, row_len, matrix)
    t = top_score(i, ii, col_height, row_len, matrix)
    b = bottom_score(i, ii, col_height, row_len, matrix)
    total = l * r * t * b
    # print(f"l-{l}, r-{r}, t-{t}, b-{b}, total-{total}")
    return total


def is_visible(i, ii, col_height, row_len, matrix):
    is_left = is_visible_left(i, ii, col_height, row_len, matrix)
    is_right = is_visible_right(i, ii, col_height, row_len, matrix)
    is_top = is_visible_top(i, ii, col_height, row_len, matrix)
    is_bottom = is_visible_bottom(i, ii, col_height, row_len, matrix)
    is_visible = is_left or is_right or is_top or is_bottom
    return is_visible


def algo_scenic_score(matrix):
    scenic_scores = []
    col_height = len(matrix)
    for i in range(1, len(matrix) - 1):
        row_len = len(matrix[i])
        for ii in range(1, len(matrix[i]) - 1):
            score = total_score(i, ii, col_height, row_len, matrix)
            scenic_scores.append(score)
            print(f"{matrix[i][ii]} - {i},{ii}, {col_height}, {row_len}, score-{score}")
    print(f"max scenic score - {max(scenic_scores)}")
    print(f"scenic_scores = {scenic_scores} - {len(scenic_scores)}")


def algo_vis(matrix):
    visible_count = 0
    col_height = len(matrix)
    for i in range(1, len(matrix) - 1):
        row_len = len(matrix[i])
        for ii in range(1, len(matrix[i]) - 1):
            is_vis = is_visible(i, ii, col_height, row_len, matrix)
            visible_count += 1 if is_vis else 0
            print(f"{matrix[i][ii]} - {i},{ii}, {col_height}, {row_len}, is_visible-{is_vis}")
    edge_vis = len(matrix[0]) * 2 + (len(matrix) - 2) * 2
    total_vis = edge_vis + visible_count
    print(
        f"total visibles - {total_vis}, edge visibles - {edge_vis}, inner visibles - {visible_count}"
    )