class Node:
    def __init__(self, key, val, prev, next):
        # We will use a node to create a linked list
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        # Need a map to track nodes, and a head and tail for ordering
        # map can expand to O(N) where N is the number of ndoes
        self.map = {}
        self.capacity = capacity
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, self.head, None)
        self.head.next = self.tail

    # Will run in O(1) time
    def get(self, key: int) -> int:
        # We will take the node if it exists and move it to the end of the linked list
        node = self.map.get(key, -1)
        if node != -1:
            # Take it out of it's current position
            node.next.prev = node.prev
            node.prev.next = node.next

            # Add it to the end
            node.next = self.tail
            node.prev = self.tail.prev
            node.prev.next = node
            self.tail.prev = node
            return node.val
        return -1

    # Will run in O(1) time
    def put(self, key: int, value: int) -> None:
        
        node = self.map.get(key, -1)

        # If the node already exists, take it out
        if node != -1:
            node.next.prev = node.prev
            node.prev.next = node.next

        # Create a node and add it to the end, update map
        node = Node(key, value, self.tail.prev, self.tail)
        node.prev.next = node
        self.tail.prev = node
        self.map[key] = node

        # If we have reached capacity, delete from the list and move the head
        if len(self.map) > self.capacity:
            del self.map[self.head.next.key]

            del_node = self.head.next
            del_node.prev.next = del_node.next
            del_node.next.prev = del_node.prev
        return None
