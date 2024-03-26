from __future__ import annotations

from typing import Any


class Item:
    def __init__(self, value: Any, next_item: Item | None = None):
        self.value = value
        self.next_item = next_item
