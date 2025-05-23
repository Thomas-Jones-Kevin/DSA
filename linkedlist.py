class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 2. Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3. Insert after a given node
    def insert_after(self, prev_node_data, data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next

        if not current:
            print("Previous node not found.")
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # 4. Delete by value
    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print("Node not found.")
            return

        prev.next = current.next
        current = None

    # 5. Delete by position (0-indexed)
    def delete_at_position(self, position):
        if position < 0:
            return

        current = self.head

        if position == 0 and current:
            self.head = current.next
            current = None
            return

        prev = None
        count = 0
        while current and count != position:
            prev = current
            current = current.next
            count += 1

        if not current:
            print("Position out of range.")
            return

        prev.next = current.next
        current = None

    # 6. Search for a value
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # 7. Get length
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 8. Reverse the list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # 9. Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.insert_after(20, 25)

ll.print_list()  # 5 -> 10 -> 20 -> 25 -> 30 -> None

print("Length:", ll.length())  # 5

ll.delete(10)
ll.print_list()  # 5 -> 20 -> 25 -> 30 -> None

ll.delete_at_position(2)
ll.print_list()  # 5 -> 20 -> 30 -> None

print("Search 20:", ll.search(20))  # True
print("Search 100:", ll.search(100))  # False

ll.reverse()
ll.print_list()  # 30 -> 20 -> 5 -> None
