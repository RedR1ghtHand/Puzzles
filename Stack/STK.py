import matplotlib.pyplot as plt


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        values = self.items

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_aspect('equal')

        for i, val in enumerate(values):
            circle = plt.Circle((0.5, i + 0.5), 0.4, color='blue', fill=True)
            ax.add_artist(circle)
            ax.text(0.5, i + 0.5, str(val), va='center', ha='center', color='white')

        ax.set_xlim(0, 1)
        ax.set_ylim(0, len(values))
        ax.axis('off')
        plt.show()


if __name__ == '__main__':
    st = Stack()
    for i in range(2, 110, 2):
        st.push(i)
    st.display()