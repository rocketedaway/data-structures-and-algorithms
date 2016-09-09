"""
Defines the public API used for different implementations of the Union-Find data structure
"""

from abc import ABCMeta, abstractmethod

class UnionFind(object):
    __metaclass__ = ABCMeta

    def __init__(self, N):
        """
        Initilize the data structure
        """
        self._component_ids = [n for n in range(N)]

    @abstractmethod
    def union(node_id, other_node_id):
        """
        Joins two distinct components which contains nodes with IDs node_id and other_node_id
        The component which contains the node with ID node_id is merged into the component containing the node with ID other_node_id

        Arguments:
            param1 (int): node_id
            param2 (int): other_node_id

        Returns:
            null
        """
        pass

    @abstractmethod
    def find(node_id):
        """
        Finds which component a node with ID node_id belongs too

        Arguments:
            param1 (int): node_id
            param2 (int): other_node_id

        Returns:
            int: Component ID
        """
        pass

    @abstractmethod
    def connected(node_id, other_node_id):
        """
        Checks if two nodes with IDs node_id and other_node_id are in the same component

        Arguments:
            param1 (int): node_id
            param2 (int): other_node_id

        Returns:
            bool: True if they are in the same component and False if they are not
        """
        pass

    @abstractmethod
    def count():
        """
        Counts how many distinct components there are

        Returns:
            int: The number of distinct components in the data structure
        """
        pass
