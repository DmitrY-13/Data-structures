from stack.exceptions import EmptyStackError


class TestNegativeCases:
    def test_getting_head_from_empty_stack(self, stack):
        try:
            stack.head
        except Exception as exc:
            assert isinstance(exc, EmptyStackError)
            assert str(exc) == 'impossible to get `head` from empty stack'

    def test_calling_pop_method_on_empty_stack(self, stack):
        try:
            stack.pop()
        except Exception as exc:
            assert isinstance(exc, EmptyStackError)
            assert str(exc) == 'impossible to call `pop` method on empty stack'
