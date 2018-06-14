
class Node(object):
    """
        This module implements the Node class as a container
        for edges to neighbor nodes.
    """

    def __init__(self, name):
        """ initialize node and set name """
        self.name = name
        self._edges = []

    def _set_name(self, name):
        self.name = name

    def _number_of_edges(self):
        """ return number of edges in this node """
        if self._edges is None:
            return 0
        return len(self._edges)

    def edges(self):
        """ return edges for this node """
        return self._edges

    def neighbors(self):
        """ return neighbors for this node """
        return [e.name for e in self.edges()]

    def add_edge(self, node):
        """ adds an edge between this node and another node """
        self._edges.append(node)

    def remove_edge(self, name):
        """ removes an edge from a node """
        for edge in self._edges:
            if edge.name == name:
                self._edges.remove(edge)

    def __str__(self):
        res = ""
        for edge in self._edges:
            try:
                res = res + edge
                res = res + "{0}, {1}".format(edge.name, edge.edges())
            except Exception as exception:
                exception = None
        return res
