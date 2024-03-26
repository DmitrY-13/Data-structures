class TestsPositiveCases:
    def test_adding(self, queue):
        queue.add(1)
        assert queue.head == 1
        assert queue.tail == 1
        assert queue.size == 1

        queue.add(2)
        assert queue.head == 1
        assert queue.tail == 2
        assert queue.size == 2

    def test_getting_head(self, queue):
        queue.add(1)
        queue.add(2)
        assert queue.head == 1

    def test_getting_tail(self, queue):
        queue.add(1)
        queue.add(2)
        assert queue.tail == 2

    def test_popping(self, queue):
        queue.add(1)
        queue.add(2)

        assert queue.pop() == 1
        assert queue.head == 2
        assert queue.size == 1
