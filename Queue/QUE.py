import matplotlib.pyplot as plt


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        values = self.items

        fig, ax = plt.subplots(figsize=(8, 3))
        ax.set_aspect('equal')

        for i, val in enumerate(values):
            circle = plt.Circle((i + 0.5, 0.5), 0.4, color='blue', fill=True)
            ax.add_artist(circle)
            ax.text(i + 0.5, 0.5, str(val), va='center', ha='center', color='white')

        ax.set_xlim(0, len(values))
        ax.set_ylim(0, 1)
        ax.axis('off')
        plt.show()


if __name__ == '__main__':
    qu = Queue()
    for i in range(2, 11, 2):
        qu.enqueue(i)
    qu.display()
