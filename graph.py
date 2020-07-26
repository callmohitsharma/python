#https://www.python-course.eu/graphs_python.php
class Graph(object):
    def __init__(self,graph_dict=None):
        if graph_dict==None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def get_vertices(self):
        return list(self.__graph_dict.keys())

    def get_edges(self):
        edges = []
        for node in self.__graph_dict.keys():
            for neighbour in self.__graph_dict[node]:
                if {neighbour,node} not in edges:
                    edges.append({node,neighbour})
        return edges
    def add_vertices(self,vertex):
        if vertex == None:
            print("Vertex value is none")
            return
        else:
            self.__graph_dict[vertex] = []

    def add_edges(self,edge):
        if edge == None:
            print("Value of edge is null")
            return
        edge = set(edge)
        (vertex1,vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict and vertex2 not in self.__graph_dict[vertex1]:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __str__(self):
        res = "Vertices are: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nEdges: "
        for k in self.get_edges():
            res += str(edges) + " "

    def find_path(self,start_vertex,end_vertex,path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path.append(start_vertex)
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return
        for node in graph[start_vertex]:
            if node not in path:
                extended_path = self.find_all_path(node,end_vertex,path)
            if extended_path:
                return extended_path
        return None

    def find_all_path(self,start_vertex,end_vertex,path=[]):
        extended_path = None
        graph = self.__graph_dict
        paths = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        for node in graph[start_vertex]:
            if node not in path:
                extended_path = self.find_all_path(node,end_vertex,path)
                for p in extended_path:
                    paths.append(p)
        return paths

    def diameter(self):
        virtices = self.get_vertices()
        pairs = [(v[i],v[j]) for i in range(len(virtices)-1) for j in range(i+1, len(virtices))]
        smallest_paths = []
        for (v1,v2) in pairs:
            get_paths = self.find_all_path(v1,v2)
            small_path = sorted(get_paths,key=len)[0]
            smallest_paths.append(small_path)
        smallest_paths.sort(key=len)
        # longest path is at the end of list,
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1])-1
        retrun diameter


if __name__ == "__main__":
    g = {
        "a" : ["d"],
        "b" : ["c"],
        "c" : ["b","c","d","e"],
        "d" : ["a","c"],
        "e" : ["c"],
        "f" : []
    }

graph = Graph(g)
print("Virtices of graph")
print(graph.get_vertices())
print("Edges of graph")
print(graph.get_edges())
print("Add vertex:")
graph.add_vertices("z")
print("Add an edge:")
graph.add_edges({"a","z"})
print("Virtices of graph")
print(graph.get_vertices())
print("Edges of graph")
print(graph.get_edges())
path = graph.find_path("c", "c")
print(path)
print('All paths from vertex "a" to vertex "b":')
path = graph.find_all_path("a", "b")
print(path)
