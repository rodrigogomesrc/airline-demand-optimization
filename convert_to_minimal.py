from graph_io import Io

io = Io(sys.argv[1])
routes = RoutesOptimization(io.get_edges())

class WeightConverter():

    def __init__(self, edges):
        self.edges = edges

    # must return the new edges
    def convert_weights():
        pass




