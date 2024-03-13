"""
Search Module

This module provides functions for searching substrings in a given string using various search methods,
including Knuth-Morris-Pratt (KMP) algorithm.
"""
from typing import Union, Tuple, Optional, Dict

from knuth_morris_pratt import kmp, kmp_reverse


def search(string: str, sub_string: Union[str, Tuple[str, ...]],
           case_sensitivity: bool = False, method: str = 'first',
           count: Optional[int] = None) -> Union[Dict[str, Tuple[int, ...]], Tuple[int, ...], None]:
    """
    Search for substrings in a given string using various search methods.

    Args:
    - string (str): The input string to search within.
    - sub_string (Union[str, Tuple[str, ...]): The substring or tuple of substrings to search for.
    - case_sensitivity (bool, optional): Whether to perform case-sensitive search (default: False).
    - method (str, optional): The search method, either 'first' (default) or 'last'.
    - count (int, optional): The maximum number of matches to find. Defaults to None.

    Returns:
    - results (Union[Dict[str, Tuple[int, ...], Tuple[int, ...], None]): The search results.
    
    If only one substring is provided, the function returns a tuple of starting positions.
    If multiple substrings are provided, the function returns a dictionary where keys are substrings,
    and values are tuples of starting positions.
    If no matches are found, the function returns None.
    """
    results = {}
    substrings = []
    if not case_sensitivity:
        string = string.lower()

    if not isinstance(sub_string, tuple):
        sub_string = (sub_string,)

    for substring in sub_string:
        if not case_sensitivity:
            substring = substring.lower()
        substrings.append(substring)

    if method == 'first':
        positions = kmp(string, substrings, count)
    elif method == 'last':
        positions = kmp_reverse(string, substrings, count)

    for item in substrings:
        if positions[item]:
            results[item] = tuple(positions[item])
        else:
            results[item] = None

    if all(val is None for val in results.values()):
        return None
    elif len(results) == 1:
        return list(results.values())[0]
    else:
        return results
