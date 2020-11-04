class Node:
    def __init__(self, key, value, next_node = None):
        self.key = key
        self.value = value
        self.next = next_node

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr is not None:
            currStr += f'{str(curr.value)} --> '
            curr = curr.next
        return currStr

    # return node with value
    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    # deletes node with given value then return node
    def delete(self, value):
        curr = self.head

        # Special case if we need to delete the head.
        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr

        prev = None

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    # insert node at the head of the list
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_at_head_or_override(self, node):
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)
