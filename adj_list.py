from queue import Queue
from stack import Stack
# lets do a graph adjacency list
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # first check that these vertices even exist
        if v1 in self.vertices and v2 in self.vertices:
            # directional
            self.vertices[v1].add(v2)
            # if you wanted to make it bidirectional or undirectional
            # repeat this but add v1 to v2
        else:
            raise IndexError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # create empty queue
        # store starting vertex in queue
        q = Queue()
        q.enqueue(starting_vertex_id)
        # create set to store visited vertices
        visited = set()
        # while queue is not empty, 
        while q.size > 0:
        #   dequeue the first vertex
            v = q.dequeue()
            # if vertex has not been visited,
            if v not in visited:
            #    do something, like mark it as visited
            #    for now just print it
                visited.add(v)
                print(v)

            #    add all of its neighbors to the end of the queue
            for next_vertex in self.get_neighbors(v):
                q.enqueue(next_vertex)


    def dft(self, starting_vertex_id):
        # create empty stack
        # store starting vertex in stack
        s = Stack()
        s.push(starting_vertex_id)
        # create set to store visited vertices
        visited = set()
        # while stack is not empty, 
        while s.size > 0:
        #   pop the first vertex
            v = s.pop()
            # if vertex has not been visited,
            if v not in visited:
            #    do something, like mark it as visited
            #    for now just print it
                visited.add(v)
                print(v)

            #    add all of its neighbors to the top of the stack
            for next_vertex in self.get_neighbors(v):
                s.push(next_vertex)
    
    def bfs(self, starting_vertex_id, target_vertex_id):
        # create an empty queue
        q = Queue()
        # enqueue THE PATH to the first vortex
        # whenever you think path, think list
        q.enqueue([starting_vertex_id])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty
        while q.size > 0:
            #dequeue the first PATH
            # grab the last vertex from the PATH
         
            # check if the vertex has not been visited
                # check is it the target
                    # if yes, return the path we grabbed
                # if not, mark as visited and 
                # add the paths to the neighbors to the back of the queue

                # make a copy of the path
                # append the neighbor to the back of the path

                #enqueue new path

        # return none (if target was not found) 

        pass

    def dfs(self, starting_vertex_id, target_vertex_id):
        pass