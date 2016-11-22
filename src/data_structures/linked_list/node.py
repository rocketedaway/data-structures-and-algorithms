"""
Implementation of the Node data structure
"""

class Node(object):
    def __init__(self, payload, next_node=None):
        super(Node, self).__init__()
        self.next_node = next_node
        self.payload = payload
