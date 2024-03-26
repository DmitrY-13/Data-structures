class TestsPositiveCases:
    def test_adding(self, stack):
        for i in range(1, 3):
            stack.add(i)
            assert stack.head == i
            assert stack.size == i

    def test_getting_head(self, stack):
        stack.add(1)
        assert stack.head == 1

    def test_popping(self, stack):
        stack.add(1)
        stack.add(2)

        assert stack.pop() == 2
        assert stack.head == 1
        assert stack.size == 1
