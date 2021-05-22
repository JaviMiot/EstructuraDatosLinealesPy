class Node:
    def __init__(self, data, next=None):
        """Class node

        Args:
            data ([type]): valor que almacena el nodo
            next ([type], optional): referencia a donde lleva el siguiente nodo. Defaults to None.
        """
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        super().__init__(data, next=next)
        self.previous = previous
