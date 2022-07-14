import sys
from cycle_finder import CycleFinder
from graph_io import Io

filename = sys.argv[1]

def order_edges_by_greater_weight(edges):
    edges.sort(key=lambda x: x[2], reverse=True)
    return edges

def is_graph_cycle(edges):
    cycle_finder = CycleFinder(edges)
    return cycle_finder.is_cycle()

io = Io(filename)
edges = io.get_edges()

edges = order_edges_by_greater_weight(edges)


def calculate_routes(edges):
    result_edges = set()
    for i in range(len(edges)):
        current_edge = {(edges[i][0], edges[i][1], edges[i][2])}
        if(not is_graph_cycle(current_edge | result_edges)):
            result_edges = result_edges | current_edge

    return result_edges


print("input edges")
print(edges)
print("\n")

print("calculated edges:")
print(calculate_routes(edges))



