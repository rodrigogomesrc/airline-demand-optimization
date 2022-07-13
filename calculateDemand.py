import sys

filename = sys.argv[1]
adjancy_matrix = []
lines = 0
matrix_filled = False

third_values = []
vertices = []
header = ""

def fill_matrix(no_fill):
    if no_fill:
        return
    for i in range(lines):
        line = [0 for i in range(lines)]
        adjancy_matrix.append(line)


def print_matrix():
    x_indice = "n => " + str([i for i in range (lines)])
    print(x_indice)
    for i in range(lines):
        print(str(i) + " => " + str(adjancy_matrix[i]))


def extract_graph_edges(adjancy_matrix):
    edges = []
    for i in range(lines):
        for j in range(lines):
            if adjancy_matrix[i][j] != 0:
                edges.append((i, j, adjancy_matrix[i][j]))
    return edges


def order_edges_by_greater_weight(edges):
    edges.sort(key=lambda x: x[2], reverse=True)
    return edges


with open(filename, 'r') as f:
    for line in f:
        if line.startswith('%'):
            header = line
        elif line.startswith('n'):
            lines = max(lines, int(line.split()[3]))
            vertices.append(line)
        elif line.startswith('e'):
            fill_matrix(matrix_filled)
            matrix_filled = True
            split_line = line.split()
            n1 = int(split_line[1])
            n2 = int(split_line[2])
            third_values.append(int(split_line[3]))
            weight = int(split_line[4])
            adjancy_matrix[n1][n2] = weight



