                      # Graph by List Method


class Stack:
    def __init__(self, list=[]):
        self.list = list

    def is_empty(self):
        return len(self.list) == 0

    def push_item(self, data):
        self.list.append(data)

    def pop(self):
        if not self.is_empty():
            self.list.pop()
        else:
            raise IndexError('Stack is empty')

    def peek(self):
        if not self.is_empty():
            return self.list[-1] 
        else:
            raise IndexError('Stack is empty')

    def size_of_stack(self):
        return print(len(self.list))


class Queue:
    def __init__(self):
        self.List = []

    def is_empty(self):
        return len(self.List) == 0

    def Enqueue(self, data):
        self.List.append(data)

    def Deqeue(self):
        if not self.is_empty():
            self.List.pop(0)
        else:
            raise IndexError('Queue underflow')

    def get_front(self):
        if not self.is_empty():
            return self.List[0]
        else:
            raise IndexError('Queue underflow')

    def get_rear(self):
        if not self.is_empty():
            return self.List[-1]
        else:
            raise IndexError('Queue underflow')

    def size(self):
        return len(self.List)


class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = {v: [] for v in range(vno)}
        self.blist = [*[False] * vno]
        self.dlist = [*[False] * vno]

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print('Invalid Vertices')

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u] = [(vertex, weight) for vertex, weight in self.adj_list[u] if vertex != v]
            self.adj_list[v] = [(vertex, weight) for vertex, weight in self.adj_list[v] if vertex != u]
        else:
            print('Invalid Vertices')

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return any(vertex == v for vertex, weight in self.adj_list[u])
        else:
            print('Invalid Vertices')

    def print_adj_list(self):
        for vertex, n in self.adj_list.items():
            print(f"V{vertex} :", *n)

    def BFS(self, s):
        V = self.blist
        Q = Queue()
        Q.Enqueue(s)
        V[s] = True
        while not Q.is_empty():
            n = Q.get_front()
            Q.Deqeue()
            print('Nodes are V', n)
            for i in self.adj_list[n]:
                A = i[0]
                if V[A] == False:
                    Q.Enqueue(A)
                    V[A] = True

    def DFS(self, s):
        V = self.dlist
        Q = Stack()
        Q.push_item(s)
        V[s] = True
        while not Q.is_empty():
            n = Q.peek()  
            Q.pop()
            print('Nodes are V', n)
            for i in self.adj_list[n]:
                A = i[0]
                if V[A] == False:
                    Q.push_item(A)
                    V[A] = True


A = Graph(6)
A.add_edge(0, 1)
A.add_edge(0, 2)
A.add_edge(1, 3)
A.add_edge(2, 3)
A.add_edge(2, 4)
A.add_edge(3, 5)
A.add_edge(3, 4)
A.print_adj_list()
A.BFS(0)
A.DFS(0)
