import sys
import os

class Io:

    def __init__(self):
        self.edges = []
        self.lines = 0
        self.third_values = {}
        self.vertices = []
        self.header = ""

    def check_if_file_exists(self, filename):
        if not os.path.isfile(filename):
            print("File " + filename + " does not exist.")
            sys.exit(1)
        return True

    def read_file(self, filename):
        if(not self.check_if_file_exists(filename)):
            return False

        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('%'):
                    self.header = line
                elif line.startswith('n'):
                    self.lines = max(self.lines, int(line.split()[3]))
                    self.vertices.append(line)
                elif line.startswith('e'):
                    split_line = line.split()
                    n1 = int(split_line[1])
                    n2 = int(split_line[2])
                    self.third_values[(n1, n2)] = int(split_line[3])

                    weight = int(split_line[4])
                    self.edges.append((n1, n2, weight))
        return True

    def set_edges(self, edges):
        self.edges = edges

    def get_edges(self):
        return self.edges

    def save_to_file(self, edges, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(self.header)
            for v in self.vertices:
                f.write(v)
            for edge in edges:
                f.write('e ' + str(edge[0]) 
                + ' ' + str(edge[1]) 
                + ' ' + str(self.third_values[(edge[0], edge[1])]) 
                +' ' + str(edge[2]) + '\n')

            f.close()
       