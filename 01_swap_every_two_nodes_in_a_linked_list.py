class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value},({self.next.__repr__()})"


def swap_every_two(list):
    head = list

    current = head

    while current is not None and current.next is not None:
        current.value, current.next.value = current.next.value, current.value
        current = current.next.next

    return head


list = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(list))
