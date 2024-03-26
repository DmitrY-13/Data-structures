import logging

import pytest

from stack import Stack

LOGGING_FORMAT = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)


@pytest.fixture
def stack():
    return Stack()
