import logging

import pytest

from queue import Queue

LOGGING_FORMAT = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)


@pytest.fixture
def queue():
    return Queue()
