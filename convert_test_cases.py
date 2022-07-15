import sys
import os
from graph_io import Io
from calculate_routes import RoutesOptimization

class WeightConverter():

    def __init__(self):
        self.edges = None
    
    def convert_weights(self, edges):
        self.edges = None
        result = [(edge[0], edge[1], 1/edge[2] * 100) for edge in edges]
        self.edges = result
        return result

    def save_converted_weights(self, filename, io_instance):
        if self.edges is None:
            print("No edges to save")
            return False
        io_instance.save_to_file(self.edges, filename)
        return True
        
if __name__ == "__main__":
    print("converting test cases...")
    
    io = Io()

    if(sys.argv[1] == "--all"):
        files = [f for f in os.listdir('./test_cases') if os.path.isfile(os.path.join('./test_cases', f))]
        for file in files:
            print("converting file: " + file)
            file_location = "./test_cases/" + file
            io.read_file(file_location)
            optimization_obj = RoutesOptimization(io.get_edges())
            edges =  optimization_obj.get_input_edges()
            converter = WeightConverter()
            result = converter.convert_weights(edges)
            converter.save_converted_weights("./converted_test_cases/" + file, io)

    else:
        filename = sys.argv[1]
        print("converting file: " + filename)
        file_location = "./test_cases/" + filename
        io.read_file(file_location)
        optimization_obj = RoutesOptimization(io.get_edges())
        edges =  optimization_obj.get_input_edges()
        converter = WeightConverter()
        result = converter.convert_weights(edges)
        converter.save_converted_weights("./converted_test_cases/" + filename, io)

    print("conversion finished")
    print("files saved to ./converted_test_cases")


