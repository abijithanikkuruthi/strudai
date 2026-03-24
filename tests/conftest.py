import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from backend.tools.registry import Registry
from backend.connection import ConnectionManager


@pytest.fixture
def registry():
    return Registry()


@pytest.fixture
def manager():
    return ConnectionManager()


@pytest.fixture
def connected_manager(manager):
    """A ConnectionManager with a mock WebSocket already connected."""
    ws = AsyncMock()
    ws.accept = AsyncMock()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(manager.connect(ws))
    return manager
