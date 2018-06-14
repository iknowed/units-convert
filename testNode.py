import unittest
from node import Node

class Testnode(unittest.TestCase):

    def test_empty(self):
        node = Node('test')
        self.assertEqual(node._number_of_edges(), 0)

    def test_add_edge(self):
        source = Node('source')
        target = Node('target')
        source.add_edge(target)
        present = target in source.edges()
        self.assertTrue(present)

    def test_remove_edge(self):
        n = Node('us')
        neighbors = ['n1', 'n2', 'n3']
        for neigh in neighbors:
            n = Node(neigh)
            n.add_edge(n)

        n.remove_edge('n2')

        for e in n.edges():
            self.assertFalse(e.name == 'n2')

    def test_edges(self):
        source = Node('source')
        target1 = Node('target1')
        source.add_edge(target1)
        target2 = Node('target2')
        source.add_edge(target2)
        target3 = Node('target3')
        source.add_edge(target3)
        for t in [target1, target2, target3]:
            present = t in source.edges()
            self.assertTrue(present)

    def test_set_name(self):
        first_name = 'first name'
        last_name = 'last name'
        node = Node(first_name)
        self.assertEqual(node.name, first_name)
        node._set_name(last_name)
        self.assertEqual(node.name, last_name)

    def test_neighbors(self):
        us = Node('us')
        n1 = Node('neighbor 1')
        n2 = Node('neighbor 2')
        n3 = Node('neighbor 3')
        for n in [n1, n2, n3]:
            us.add_edge(n)
        neighbors = us.neighbors()
        self.assertEqual(len(neighbors), 3)
        for n in [n1, n2, n3]:
            self.assertTrue(n.name in neighbors)

if __name__ == '__main__':
    unittest.main()
