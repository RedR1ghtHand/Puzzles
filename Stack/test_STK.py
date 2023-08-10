import pytest
from Stack.STK import Stack


class TestStack:
    test_case = [5, 10, 20, 40, 80]

    def test_empty_stack(self):
        st = Stack()

        assert st.items == []
        assert st.is_empty() is True
        with pytest.raises(IndexError):
            st.pop()

    def test_push(self):
        st = Stack()
        for i in self.test_case:
            st.push(i)

        assert st.items == self.test_case

    def test_pop(self):
        st = Stack()
        for i in self.test_case:
            st.push(i)

        for i in self.test_case[::-1]:
            assert st.pop() == i

        # for i in self.test_case:
        #    st.push(i)
        #    assert st.pop() == i

        assert st.is_empty() is True

    def test_size(self):
        st = Stack()
        for i in self.test_case:
            st.push(i)

        assert st.size() == len(self.test_case)

    def test_peek(self):
        st = Stack()
        for i in self.test_case:
            st.push(i)
            assert st.peek() == i







