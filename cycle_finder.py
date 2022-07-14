class CycleFinder:

    def __init__(self, edges):
        self.adjacency_list = self.get_adjacency_list(edges)
        self.stack = []
        self.vertices_visited_info = {}
        self.cycle_exists = False

        for edge in edges:
            self.vertices_visited_info[edge[0]] = False
            self.vertices_visited_info[edge[1]] = False
           
    def get_adjacency_list(self, edges):
        adjacency_list = {}
        for edge in edges:
            if edge[0] not in adjacency_list:
                adjacency_list[edge[0]] = []

            adjacency_list[edge[0]].append(edge[1])
            if edge[1] not in adjacency_list:
                adjacency_list[edge[1]] = []

            adjacency_list[edge[1]].append(edge[0])
        
        return adjacency_list
    
    def print_adjacency_list(self):
        for key in self.adjacency_list:
            print(key, self.adjacency_list[key])
        print("\n")

    def is_cycle(self):
        self.search(list(self.adjacency_list.keys())[0])
        return self.cycle_exists

    def search(self, vertex):
        self.vertices_visited_info[vertex] = True
        self.stack.append(vertex)

        for v in self.adjacency_list[vertex]:
            if not self.vertices_visited_info[v]:
                self.search(v)

            elif self.stack[-2] != v:
                self.cycle_exists = True
                return
            
        self.stack.pop()



    

