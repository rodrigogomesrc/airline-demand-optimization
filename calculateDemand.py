import sys

filename = sys.argv[1]
adjancy_matrix = []
lines = 0
matrix_filled = False

def fill_matrix(no_fill):
    if no_fill:
        return
    for i in range(lines):
        line = [0 for i in range(lines)]
        adjancy_matrix.append(line)


def print_matrix():
    for i in range(lines):
        print(adjancy_matrix[i])


with open(filename, 'r') as f:
    for line in f:
        if line.startswith('%'):
            continue
        elif line.startswith('n'):
            lines = max(lines, int(line.split()[3]))
        elif line.startswith('e'):
            fill_matrix(matrix_filled)
            matrix_filled = True
            split_line = line.split()
            n1 = int(split_line[1])
            n2 = int(split_line[2])
            weight = int(split_line[4])
            adjancy_matrix[n1][n2] = weight
            adjancy_matrix[n2][n1] = weight

