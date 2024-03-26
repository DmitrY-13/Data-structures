from queue.exceptions import EmptyQueueError


class TestNegativeCases:
    def test_getting_head_from_empty_stack(self, queue):
        try:
            queue.head
        except Exception as exc:
            assert isinstance(exc, EmptyQueueError)
            assert str(exc) == 'impossible to get `head` from empty queue'

    def test_getting_tail_from_empty_stack(self, queue):
        try:
            queue.tail
        except Exception as exc:
            assert isinstance(exc, EmptyQueueError)
            assert str(exc) == 'impossible to get `tail` from empty queue'

    def test_calling_pop_method_on_empty_stack(self, queue):
        try:
            queue.pop()
        except Exception as exc:
            assert isinstance(exc, EmptyQueueError)
            assert str(exc) == 'impossible to call `pop` method on empty queue'
