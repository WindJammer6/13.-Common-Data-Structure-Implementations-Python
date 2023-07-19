class AdjacencyListDirectedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}

        for start, end in self.edges:
            if start in self.graph_dictionary:
                self.graph_dictionary[start].append(end)
            else:
                self.graph_dictionary[start] = [end]
            
        for start, end in self.edges:
            if end not in self.graph_dictionary:
                self.graph_dictionary[end] = []

    def add_node(self, node):
        if node in self.graph_dictionary:
            print(node, "is already present in the Graph Data Structure")

        else:
            self.graph_dictionary[node] = []

    def add_edge(self, startnode, endnode):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary[startnode].append(endnode)

    def delete_node(self, node):
        if node not in self.graph_dictionary:
            print(node, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary.pop(node)
            
            for i in self.graph_dictionary:
                value_list = self.graph_dictionary[i]
                if node in value_list:
                    value_list.remove(node)

    def delete_edge(self, startnode, endnode):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        else:
            if endnode in self.graph_dictionary[startnode]:
                self.graph_dictionary[startnode].remove(endnode)
            else:
                print("No such edge exists that is pointing in the direction from", startnode, "to", endnode)

    def breadth_first_search(self, rootnode):
 
        queue_list = []
        visited = []
 
        queue_list.append(rootnode)
 
        while queue_list:
            s = queue_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i not in visited and i not in queue_list:
                        queue_list.append(i)

        return visited
    
    def depth_first_search(self, rootnode):
 
        stack_list = []
        visited = []
 
        stack_list.insert(0, rootnode)
 
        while stack_list:
            s = stack_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i not in visited and i not in stack_list:
                        stack_list.insert(0, i)

        return visited
    
    def get_all_possible_paths(self, startnode, endnode, path=[]):

        path = path + [startnode]

        if startnode == endnode:
            return [path]
        
        all_possible_paths = []

        for node in self.graph_dictionary[startnode]:
            if node not in path:
                new_paths = self.get_all_possible_paths(node, endnode, path)
                for p in new_paths:
                    all_possible_paths.append(p)

        return all_possible_paths

    def get_shortest_path(self, startnode, endnode, path=[]):
        
        #Appending the 'startnode' element to the 'path' List
        path = path + [startnode]

        #When we do recursion, we must always define the simplest cases first for our recursion loops to 
        #'bounce' back from, which will be if the 'startnode' also happens to be the 'endnode', then we
        #will just return the path List
        if startnode == endnode:
            return path
        
        shortest_path = None

        for node in self.graph_dictionary[startnode]:
            if node not in path:
                sp = self.get_shortest_path(node, endnode, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path
      
    def __repr__(self):
        return '{}'.format(self.graph_dictionary)
    

if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    routes_graph = AdjacencyListDirectedGraph(routes)
    print(routes_graph)

    routes_graph.add_node("Singapore")
    print(routes_graph)

    routes_graph.add_edge("Singapore", "Toronto")
    print(routes_graph)

    routes_graph.delete_node("Singapore")
    print(routes_graph)

    # routes_graph.delete_edge("Mumbai", "Dubai")
    # print(routes_graph)
    
    print("Following is the Breadth-First Search")
    print(routes_graph.breadth_first_search('Mumbai'))

    print("Following is the Depth-First Search")
    print(routes_graph.depth_first_search('Mumbai'))


    start = "Mumbai"
    end = "New York"

    print(f"Paths between {start} and {end}: ", routes_graph.get_all_possible_paths(start, end))

    print(f"Shortest path (in terms of number of stops) between {start} and {end}: ", routes_graph.get_shortest_path(start, end))
