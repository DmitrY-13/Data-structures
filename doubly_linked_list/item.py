from __future__ import annotations

from typing import Any


class Item:
    def __init__(self, value=None, previous_item: Item | None = None):
        self.value: Any = value
        self.previous_item: Item | None = previous_item
        self.next_item: Item | None = None
