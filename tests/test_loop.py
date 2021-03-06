import pytest
import asyncio

from async_retrying import retry, RetryError


@pytest.mark.run_loop
@asyncio.coroutine
def test_immutable_with_kwargs(loop):

    @retry(loop='_loop', immutable=True, kwargs=True, fatal_exceptions=KeyError)
    @asyncio.coroutine
    def coro(a, *, _loop):
        a.pop('a')
        raise RuntimeError

    with pytest.raises(RetryError):
        yield from coro(a={'a': 'a'}, _loop=loop)
