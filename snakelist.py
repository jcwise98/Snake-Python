class SNode:
    def __init__(self, xpos=10, ypos=300):
        self.x = xpos
        self.y = ypos
        self.xprev = None
        self.yprev = None
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.length = 1