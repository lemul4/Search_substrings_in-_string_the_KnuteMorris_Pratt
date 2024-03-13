"""
timing_decorator Module
"""
import time
from typing import Any, Callable


def timing_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures the execution time of a function and logs it.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """

    def wrapper(*args, **kwargs) -> Any:
        """
        The wrapper function that measures execution time, logs it, and calls the original function.

        Args:
            *args: Positional arguments for the decorated function.
            **kwargs: Keyword arguments for the decorated function.

        Returns:
            Any: The result of the decorated function.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.2f} seconds")
        return result

    return wrapper
