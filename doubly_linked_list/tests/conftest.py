import logging

import pytest

from doubly_linked_list import DoublyLinkedList

LOGGING_FORMAT = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)


@pytest.fixture
def doubly_linked_list():
    return DoublyLinkedList()


@pytest.fixture
def doubly_linked_list_filled_012():
    doubly_linked_list = DoublyLinkedList()
    for i in range(3):
        doubly_linked_list.add(i)
    return doubly_linked_list
