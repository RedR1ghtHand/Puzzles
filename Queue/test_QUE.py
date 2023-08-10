import pytest
from Queue.QUE import Queue


class TestQueue:
    test_case = [2, 4, 8,  16, 32]

    def test_empty_queue(self):
        qe = Queue()

        assert qe.items == []
        assert qe.is_empty() is True
        with pytest.raises(IndexError):
            qe.dequeue()

    def test_enqueue(self):
        qe = Queue()
        for i in self.test_case:
            qe.enqueue(i)

        assert qe.items == self.test_case

    def test_dequeue(self):
        qe = Queue()
        for i in self.test_case:
            qe.enqueue(i)

        for i in self.test_case:
            assert qe.dequeue() == i

        assert qe.is_empty() is True

    def test_size(self):
        qe = Queue()
        for i in self.test_case:
            qe.enqueue(i)

        assert qe.size() == len(self.test_case)

    def test_front(self):
        qe = Queue()
        for i in self.test_case:
            qe.enqueue(i)
            assert qe.front() == self.test_case[0]

