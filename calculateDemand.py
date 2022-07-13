import sys

filename = sys.argv[1]
edges = []
lines = 0

third_values = []
vertices = []
header = ""

def order_edges_by_greater_weight(edges):
    edges.sort(key=lambda x: x[2], reverse=True)
    return edges

# Todo: implement the algorithm
def check_cycle_in_graph(edges):
    return False


with open(filename, 'r') as f:
    for line in f:
        if line.startswith('%'):
            header = line
        elif line.startswith('n'):
            lines = max(lines, int(line.split()[3]))
            vertices.append(line)
        elif line.startswith('e'):
            split_line = line.split()
            n1 = int(split_line[1])
            n2 = int(split_line[2])
            third_values.append(int(split_line[3]))
            weight = int(split_line[4])
            edges.append((n1, n2, weight))

edges = order_edges_by_greater_weight(edges)
print(edges)