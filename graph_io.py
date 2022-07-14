import sys

class Io:

    def __init__(self, filename):
        self.filename = filename
        self.edges = []
        self.lines = 0
        self.third_values = []
        self.vertices = []
        self.header = ""
        self.read_file()

    def read_file(self):
        with open(self.filename, 'r') as f:
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
                    self.third_values.append(int(split_line[3]))
                    weight = int(split_line[4])
                    self.edges.append((n1, n2, weight))

    def get_edges(self):
        return self.edges

    def save_result(self, edges):
        pass