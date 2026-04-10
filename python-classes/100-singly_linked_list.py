#!/usr/bin/python3
"""Module defining a Node and a Singly Linked List."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node with data and an optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with integer validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with Node or None validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Define the print behavior for the linked list."""
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position (increasing)."""
        new_node = Node(value)

        # Case 1: List is empty or new value is smaller than the head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Find the position in the middle or end
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
