class Node:
    def __init__(self, data, next=None):
        """Class node

        Args:
            data ([type]): valor que almacena el nodo
            next ([type], optional): referencia a donde lleva el siguiente nodo. Defaults to None.
        """
        self.data = data
        self.next = next
