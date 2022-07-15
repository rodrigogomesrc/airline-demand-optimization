import sys
import time
from cycle_finder import CycleFinder
from graph_io import Io
from stats import Stats
import os

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

    # using kruskal algorithm
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
    print("calculating...")
    io = Io()
    stats = Stats()
    if(sys.argv[1] == "--all"):
        files = [f for f in os.listdir('./test_cases') if os.path.isfile(os.path.join('./test_cases', f))]
        files.sort()
        for file in files:
            start_time = time.time()
            print("calculating for file: " + file)
            file_location = "./test_cases/" + file
            io.read_file(file_location)
            optimization_obj = RoutesOptimization(io.get_edges())
            routes = RoutesOptimization(io.get_edges())
            result = routes.calculate_routes()
            io.save_to_file(result, "./results/" + file)
            end_time = time.time()
            print("Time taken: %.2f ms" %((end_time - start_time) * 1000))
            stats.add_data(file, (end_time - start_time) * 1000)

        stats.plot_and_save("./stats/stats.png")
        print("chart with executions times saved to ./stats/stats.png")

    else:
        start_time = time.time()
        filename = sys.argv[1]
        print("calculating for file: " + filename)
        file_location = "./test_cases/" + filename
        io.read_file(file_location)
        routes = RoutesOptimization(io.get_edges())
        result = routes.calculate_routes()
        io.save_to_file(result, "./results/" + filename)
        end_time = time.time()
        print("Time taken: %.2f ms" %((end_time - start_time) * 1000))

    print("done")
    print("files saved to ./results")



