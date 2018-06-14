import unittest
from graph import Graph
from node import Node

class TestGraph(unittest.TestCase):

    def test_empty(self):
        self.g = Graph()
        self.assertEqual(self.g._number_of_nodes(), 0)

    def test_add(self):
        self.g = Graph()
        n = Node('test1')
        self.g.add_node(n)
        self.assertEqual(self.g._number_of_nodes(), 1)

    def test_number_of_nodes(self):
        self.g = Graph()
        n = Node('test1')
        self.g.add_node(n)
        n = Node('test2')
        self.g.add_node(n)
        n = Node('test3')
        self.g.add_node(n)
        self.assertEqual(self.g._number_of_nodes(), 3)

    def test_nodes_fn(self):
        self.g = Graph()
        names = ['test1', 'test2', 'test3']
        nodes = set()
        for name in names:
           no = Node(name)
           self.g.add_node(no)
           nodes.add(no)
        self.assertTrue(nodes == set(self.g.nodes().keys()))

    def test_node_by_name(self):
        self.g = Graph()
        n = Node('test1')
        self.g.add_node(n)
        n = Node('test2')
        self.g.add_node(n)
        n = Node('test3')
        self.g.add_node(n)
        n = self.g._node_by_name('test2')
        self.assertEqual(n.name, 'test2')

    def test_node_edges_have_edges(self):
        self.g = Graph()
        a = Node('A')
        edge_nodes = ['B', 'C', 'D']
        s = set()
        for edge_node in edge_nodes:
            s.add(edge_node)
            n = Node(edge_node)
            a.add_edge(n)

        self.assertTrue(s == set([e.name for e in a.edges()]))

    def test_remove_node(self):
        self.g = Graph()
        name = 'A'
        a = Node(name)
        self.g.add_node(a)
        self.g.remove_node(name)
        a = self.g._node_by_name(name)
        self.assertTrue(a == None)

    def test_graph_from_dict(self):
        edges = ['B', 'C', 'D']
        gdict = {}
        self.g = Graph()
        gdict['A'] = edges
        self.g.graph_from_dict(gdict)
        self.assertTrue('A' in [n.name for n in self.g._nodes])
        a = self.g._node_by_name('A')
        self.assertTrue(set(edges) == set([e.name for e in a.edges()]))

    def test_dijkstras(self):
        graph = {}
        graph['B'] = ['C']
        graph['C'] = ['D']
        graph['D'] = ['E']
        graph['E'] = ['F']
        graph['F'] = ['Z']

        graph['G'] = ['H']
        graph['H'] = ['I']
        graph['I'] = ['J']
        graph['J'] = ['K']
        graph['K'] = ['L']
        graph['L'] = ['M']
        graph['M'] = ['N']
        graph['N'] = ['Z']

        graph['O'] = ['P']
        graph['P'] = ['Q']
        graph['Q'] = ['R']
        graph['R'] = ['S']
        graph['S'] = ['T']
        graph['T'] = ['U']
        graph['U'] = ['V']
        graph['V'] = ['W']
        graph['W'] = ['X']
        graph['X'] = ['Y']
        graph['Y'] = ['Z']
        graph['Z'] = None

        graph['A'] = ['B', 'G', 'O']

        self.g = Graph()

        self.g.graph_from_dict(graph)

        self.paths = self.g.dijkstra('A', 'Z')
        correct = ['A', 'B', 'C', 'D', 'E', 'F', 'Z']
        #path = [p.name for p in self.paths[min(self.paths.keys())][0]]
        path = [p.name for p in self.paths]
        self.assertEqual(path, correct)

if __name__ == '__main__':
    unittest.main()
