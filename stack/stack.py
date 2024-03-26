import logging
from typing import Any

from stack.exceptions import EmptyStackError
from stack.item import Item

logger = logging.getLogger(__name__)


class Stack:
    def __init__(self):
        self._head: Item | None = None
        self._size: int = 0

    @property
    def head(self) -> Any:
        logger.info('getting `head`')
        if not self._head:
            logger.error('impossible to get `head` from empty stack')
            raise EmptyStackError('impossible to get `head` from empty stack')

        logger.info('`head` is got')
        return self._head.value

    @property
    def size(self) -> int:
        return self._size

    def add(self, value) -> None:
        logger.info('adding value')
        self._size += 1

        previous_head = self._head
        self._head = Item(value, previous_head)

        logger.info('value is added')
        logger.debug(self)

    def pop(self) -> Any:
        logger.info('popping value')
        if not self._head:
            logger.error('impossible to call `pop` method on empty stack')
            raise EmptyStackError('impossible to call `pop` method on empty stack')

        self._size -= 1

        value = self._head.value

        self._head = self._head.next_item

        logger.info('value is popped')
        logger.debug(self)
        return value

    def __repr__(self):
        result = '<->['

        current_item = self._head
        while current_item:
            result += repr(current_item.value)

            current_item = current_item.next_item

            if current_item:
                result += ', '

        result += ']'

        return result
