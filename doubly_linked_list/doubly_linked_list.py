import logging
from typing import Any

from doubly_linked_list.item import Item
from doubly_linked_list.exceptions import EmptyDoublyLinkedListError

logger = logging.getLogger(__name__)


class DoublyLinkedList:
    def __init__(self):
        self._first_item: Item | None = None
        self._last_item: Item | None = None
        self._size: int = 0

    @property
    def first_value(self) -> Any:
        logger.info('getting `first_value`')
        if not self._first_item:
            logger.error('impossible to get `first_value` from empty doubly linked list')
            raise EmptyDoublyLinkedListError('impossible to get `first_value` from empty doubly linked list')

        logger.info('`first_value` got successful')
        return self._first_item.value

    @property
    def last_value(self) -> Any:
        logger.info('getting `last_value`')
        if not self._last_item:
            logger.error('impossible to get `last_value` from empty doubly linked list')
            raise EmptyDoublyLinkedListError('impossible to get `last_value` from empty doubly linked list')

        logger.info('`last_value` got successful')
        return self._last_item.value

    def add(self, value: Any) -> None:
        logger.info('adding value')
        self._size += 1

        if self._first_item is None:
            self._first_item = Item(value)
            self._last_item = self._first_item
            return

        new_item = Item(value, self._last_item)
        self._last_item.next_item = new_item
        self._last_item = new_item
        logger.info('value added successful')

    def pop(self, index: int | None = None) -> Any:
        logger.info('popping value')
        if index is None:
            logger.info('`index` is None, new `index` value is last index')
            index = self._size - 1

        item = self._get_item(index)
        previous_item = item.previous_item
        next_item = item.next_item

        if previous_item:
            previous_item.next_item = next_item
        else:
            self._first_item = self._first_item.next_item

        if next_item:
            next_item.previous_item = previous_item
        else:
            self._last_item = self._last_item.previous_item

        self._size -= 1

        logger.info('value popped successful')
        logger.debug(self)
        return item.value

    def __getitem__(self, index: int) -> Any:
        logger.info('getting value')
        value = self._get_item(index).value
        logger.info('value got successful')
        return value

    def _get_item(self, index: int) -> Item:
        logger.info('getting item')
        from_last = False

        if index < 0:
            index = self._size + index
            from_last = True

        if index > self._size - 1 or index < 0:
            logger.error('index out of range')
            raise IndexError('index out of range')

        if from_last:
            item = self._last_item
            for _ in range(self._size - index - 1):
                item = item.previous_item
            return item

        item = self._first_item
        for _ in range(index):
            item = item.next_item

        logger.info('item got successful')
        return item

    def __repr__(self):
        result = '['

        current_item = self._first_item
        while current_item:
            result += repr(current_item.value)

            current_item = current_item.next_item

            if current_item:
                result += ', '

        result += ']'

        return result
