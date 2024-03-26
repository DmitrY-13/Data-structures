class TestsPositiveCases:
    def test_adding(self, doubly_linked_list):
        for i in range(3):
            doubly_linked_list.add(i)
            assert doubly_linked_list[i] == i

    def test_getting_value_with_negative_index(self, doubly_linked_list):
        for i in range(3):
            doubly_linked_list.add(i)
            assert doubly_linked_list[-1] == i
            assert doubly_linked_list[-(i + 1)] == 0

        assert doubly_linked_list[-2] == 1

    def test_getting_first_value(self, doubly_linked_list_filled_012):
        assert doubly_linked_list_filled_012.first_value == 0

    def test_getting_last_value(self, doubly_linked_list_filled_012):
        assert doubly_linked_list_filled_012.last_value == 2

    def test_popping_value(self, doubly_linked_list_filled_012):
        for i in reversed(range(3)):
            assert doubly_linked_list_filled_012.pop() == i

    def test_popping_value_with_index(self, doubly_linked_list_filled_012):
        assert doubly_linked_list_filled_012.pop(1) == 1

    def test_popping_value_with_negative_index(self, doubly_linked_list_filled_012):
        assert doubly_linked_list_filled_012.pop(-2) == 1
