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
def is_graph_cycle(edges):
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


def calculate_routes(edges):
    result_edges = set()
    for i in range(len(edges)):
        current_edge = {(edges[i][0], edges[i][1])}
        if(not is_graph_cycle(result_edges | current_edge)):
            result_edges = result_edges | current_edge

    return result_edges

print(calculate_routes(edges))


