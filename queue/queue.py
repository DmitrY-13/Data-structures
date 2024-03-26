import logging
from typing import Any

from queue.exceptions import EmptyQueueError
from queue.item import Item

logger = logging.getLogger(__name__)


class Queue:
    def __init__(self):
        self._head: Item | None = None
        self._tail: Item | None = None
        self._size: int = 0

    @property
    def head(self) -> Any:
        logger.info('getting `head`')
        if not self._head:
            logger.error('impossible to get `head` from empty queue')
            raise EmptyQueueError('impossible to get `head` from empty queue')

        logger.info('`head` is got')
        return self._head.value

    @property
    def tail(self) -> Any:
        logger.info('getting `tail`')
        if not self._tail:
            logger.error('impossible to get `tail` from empty queue')
            raise EmptyQueueError('impossible to get `tail` from empty queue')

        logger.info('`tail` is got')
        return self._tail.value

    @property
    def size(self) -> int:
        return self._size

    def add(self, value) -> None:
        logger.info('adding value')
        self._size += 1

        if not self._head:
            self._head = Item(value)
            self._tail = self._head
        else:
            new_item = Item(value)
            self._tail.next_item = new_item
            self._tail = new_item

        logger.info('value is added')
        logger.debug(self)

    def pop(self) -> Any:
        logger.info('popping value')
        if not self._head:
            logger.error('impossible to call `pop` method on empty queue')
            raise EmptyQueueError('impossible to call `pop` method on empty queue')

        self._size -= 1

        value = self._head.value

        self._head = self._head.next_item

        if not self._head:
            self._tail = None

        logger.info('value is popped')
        logger.debug(self)
        return value

    def __repr__(self):
        result = '<-['

        current_item = self._head
        while current_item:
            result += repr(current_item.value)

            current_item = current_item.next_item

            if current_item:
                result += ', '

        result += ']<-'

        return result
