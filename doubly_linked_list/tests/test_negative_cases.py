from doubly_linked_list.exceptions import EmptyDoublyLinkedListError


class TestNegativeCases:
    def test_getting_value_with_out_of_range_index(self, doubly_linked_list):
        try:
            doubly_linked_list[0]
        except Exception as exc:
            assert isinstance(exc, IndexError)
            assert str(exc) == 'index out of range'

    def test_getting_value_with_out_of_range_negative_index(self, doubly_linked_list):
        try:
            doubly_linked_list[-1]
        except Exception as exc:
            assert isinstance(exc, IndexError)
            assert str(exc) == 'index out of range'

    def test_getting_first_value_from_empty_doubly_linked_list(self, doubly_linked_list):
        try:
            doubly_linked_list.first_value
        except Exception as exc:
            assert isinstance(exc, EmptyDoublyLinkedListError)
            assert str(exc) == 'impossible to get `first_value` from empty doubly linked list'

    def test_getting_last_value_from_empty_doubly_linked_list(self, doubly_linked_list):
        try:
            doubly_linked_list.last_value
        except Exception as exc:
            assert isinstance(exc, EmptyDoublyLinkedListError)
            assert str(exc) == 'impossible to get `last_value` from empty doubly linked list'

    def test_popping_value_from_empty_doubly_linked_list(self, doubly_linked_list):
        try:
            doubly_linked_list.pop()
        except Exception as exc:
            assert isinstance(exc, IndexError)
            assert str(exc) == 'index out of range'

    def test_popping_value_with_out_of_range_index(self, doubly_linked_list):
        try:
            doubly_linked_list.pop(0)
        except Exception as exc:
            assert isinstance(exc, IndexError)
            assert str(exc) == 'index out of range'

    def test_popping_value_with_out_of_range_negative_index(self, doubly_linked_list):
        try:
            doubly_linked_list.pop(-1)
        except Exception as exc:
            assert isinstance(exc, IndexError)
            assert str(exc) == 'index out of range'
