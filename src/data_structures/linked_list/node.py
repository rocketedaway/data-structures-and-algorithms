class Node(object):
    def __init__(self, payload, next = None):
        super(Node, self).__init__()
        self.next = next
        self.payload = payload
