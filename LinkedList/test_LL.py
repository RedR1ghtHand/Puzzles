from LinkedList.LL import LinkedList


class TestLL:

    def test_append(self):
        ll = LinkedList()
        assert ll.head is None
        assert ll.tail is None

        ll.append(2)
        assert ll.head.data == 2
        assert ll.tail is not None

    def test_append_complex_case(self):
        ll = LinkedList()
        assert ll.head is None
        assert ll.tail is None

        elements = [4, 7, 1, 9, 2]
        for elem in elements:
            ll.append(elem)

        current = ll.head
        index = 0
        while current is not None:
            assert current.data == elements[index]
            current = current.next
            index += 1

        assert ll.head.data == elements[0]
        assert ll.tail.data == elements[-1]

    def test_search(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(5)
        ll.append(8)

        assert ll.search(2) == 2
        assert ll.search(5) == 5
        assert ll.search(8) == 8
        assert ll.search(10) is None

    def test_search_large_case(self):
        ll = LinkedList()
        import random

        elements = list(range(1, 1001))
        random.shuffle(elements)
        for elem in elements:
            ll.append(elem)

        search_value = random.choice(elements)
        assert ll.search(search_value) == search_value

    def test_search_huge_case(self):
        ll = LinkedList()
        import random
        elements = list(range(1, 1001))
        random.shuffle(elements)
        for elem in elements * 1000:
            ll.append(elem)

        search_value = random.choice(elements)
        assert ll.search(search_value) == search_value

    def test_remove(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(5)
        ll.append(8)

        ll.remove(5)
        assert ll.head.data == 2
        assert ll.head.next.data == 8
        assert ll.tail.data == 8

        ll.remove(2)
        assert ll.head.data == 8
        assert ll.tail.data == 8

        ll.remove(8)
        assert ll.head is None
        assert ll.tail is None

