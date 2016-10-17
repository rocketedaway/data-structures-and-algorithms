class Node(object):
    def __init__(self, payload, next = None):
        self.next = next
        self.payload = payload
        super(Node, self).__init__()

