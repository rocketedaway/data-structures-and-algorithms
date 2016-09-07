"""
Defines the public API used for different implementations of the Disjoint Set data structure
"""

from abc import ABCMeta, abstractmethod

class DisjointSet(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def union(member_id, other_member_id):
        """
        Joins two distinct sets which contains members with IDs member_id and other_member_id

        Arguments:
            param1 (int): member_id
            param2 (int): other_member_id

        Returns:
            Null
        """
        pass

    @abstractmethod
    def find(member_id):
        """
        Finds which set a member with ID member_id belongs too

        Arguments:
            param1 (int): member_id
            param2 (int): other_member_id

        Returns:
            int: Set ID
        """
        pass

    @abstractmethod
    def connected(member_id, other_member_id)):
        """
        Checks if two members with IDs member_id and other_member_id are in the same set

        Arguments:
            param1 (int): member_id
            param2 (int): other_member_id

        Returns:
            bool: True if they are in the same set and False if they are not
        """
        pass

    @abstractmethod
    def count():
        """
        Counts how many distinct sets there are

        Returns:
            int: The number of distinct subsets
        """
        pass
