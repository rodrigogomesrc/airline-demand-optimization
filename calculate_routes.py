import sys
from cycle_finder import CycleFinder
from graph_io import Io

class RoutesOptimization():
    def __init__(self, edges):
        self.input_edges = edges

    def get_input_edges(self):
        return self.input_edges

    def order_edges_by_greater_weight(self, edges):
        edges.sort(key=lambda x: x[2], reverse=True)

    def is_graph_cycle(self, edges):
        cycle_finder = CycleFinder(edges)       
        return cycle_finder.is_cycle()

    def calculate_routes(self):
        edges = self.input_edges.copy()
        self.order_edges_by_greater_weight(edges)
        result_edges = set()
        for i in range(len(edges)):
            current_edge = {(edges[i][0], edges[i][1], edges[i][2])}
            if(not self.is_graph_cycle(current_edge | result_edges)):
                result_edges = result_edges | current_edge

        return result_edges

if __name__ == "__main__":
    io = Io(sys.argv[1])
    routes = RoutesOptimization(io.get_edges())
    
    print("Input edges:")
    print(routes.get_input_edges())
    print("\n")

    print("calculated edges:")
    print(routes.calculate_routes())



