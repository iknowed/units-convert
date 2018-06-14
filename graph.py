import heapq
from node import Node

class Graph(object):

    """
        This module implements the Graph class as a container
        for nodes.

    """

    def __init__(self):
        """ Graph constructor """
        self._nodes = {}

    def graph_from_dict(self, gdict):
        """
            instantiate graph from dict

            Args:
                graph(dict) a dict representation of the graph in the form:
                { 'Node' : [ 'Edge1', 'Edge2', 'Edge3' ] }
        """
        # iterate over nodes in gdict
        # graph_node that we're processing
        # edge_node that we're adding to gn
        for node in gdict:
            graph_node = Node(node)

            # only add node once
            if graph_node not in self._nodes:
                self.add_node(graph_node)

            # if there are edges to add, add them
            if gdict[node] is not None:
                for edge in gdict[node]:

                    # create the node
                    edge_node = Node(edge)

                    # add it as an edge to the graph node
                    graph_node.add_edge(edge_node)

                # add an edged node to the graph
                self.add_node(graph_node)

    def nodes(self):
        """ public accessor function for _nodes list """
        return self._nodes

    def _number_of_nodes(self):
        """ returns number of nodes in the graph """
        if self._nodes is None:
            return 0
        return len(self._nodes)

    def add_node(self, node):
        """
            adds a node to the graph if not in graph

            Args:
                name(str) node object to add
        """
        if node not in self._nodes:
            self._nodes[node] = 1

    def remove_node(self, name):
        """
            remove node from the graph

            Args:
                name(str) name of node to remove
        """
        node = self._node_by_name(name)
        if node is not None:
            del self._nodes[node]

    def _node_by_name(self, name):
        """
            retrieve node object from graph by name

            Args:
                name(str) name of node to retrieve
        """
        for node in self._nodes:
            if node.name == name:
                return node
        return None

    def dijkstra(self, source, target):
        """
            Dijkstra's algorithm implemented with a queue
            Args:
                source (str) source node name
                target (str) target node name

            Returns:
                list: list of list of paths by path length/cost
        """

        # initial cost, source node, and empty path primes the queue
        queue = [(0, source, [])]

        # hold nodes we've seen
        seen = set()

        # so long as there are more nodes to process
        while len(queue):

            # pop the queue
            (cost, name, path) = heapq.heappop(queue)

            # fetch the node
            node = self._node_by_name(name)

            if node is None:
                continue

            # if this node is new, add its neighbors to the queue
            if node not in seen:

                # add to path
                path = path + [node]

                # mark seen
                seen.add(node)

                # did we find a valid path?
                if name == target:
                    return path

                # queue up visits to neighbors
                for nxt in node.edges():
                    heapq.heappush(queue, (cost + 1, nxt.name, path))
        return paths


    def __str__(self):
        res = ""
        for node in self._nodes:
            try:
                res = res + "{0}: {1}\n".format(node.name, str([edge.name for edge in node.edges()]))
            except Exception as exception:
                exception = None
        return res
