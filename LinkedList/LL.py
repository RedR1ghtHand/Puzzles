import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current = current.next
        return None

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next

        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111)

        x = list(range(len(nodes)))
        y = [0] * len(nodes)

        ax.scatter(x, y, s=100, c='blue', marker='o')

        for _ in range(len(nodes) - 1):
            arrow = FancyArrowPatch((x[i], y[i]), (x[i+1], y[i+1]), arrowstyle='->', color='black')
            ax.add_patch(arrow)

        ax.set_xticks(x)
        ax.set_xticklabels(nodes)
        ax.set_yticks([])
        ax.set_xlabel("Data")

        plt.show()


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(2, 11, 2):
        ll.append(i)
    ll.display()
