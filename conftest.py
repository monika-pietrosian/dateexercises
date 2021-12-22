import pytest

@pytest.fixture(scope = 'function')
def func_scope():
    """A function scope fixture."""

@pytest.fixture(scope = 'module')
def mod_scope():
    """A function scope fixture."""

@pytest.fixture(scope = 'class')
def class_scope():
    """A function scope fixture."""
