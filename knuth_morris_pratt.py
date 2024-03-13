"""
Knuth–Morris–Pratt Module

This module provides functions for pattern searching in strings using the Knuth-Morris-Pratt (KMP) algorithm.
"""

from typing import List, Optional, Dict


def kmp(string: str, substrings: List[str], count: Optional[int] = None) -> Dict[str, List[int]]:
    """
    Search for substrings in a given string from the beginning using the Knuth-Morris-Pratt (KMP) algorithm.
    
    Args:
    - string (str): The input string to search within.
    - substrings (List[str]): A list of substrings to search for in the input string.
    - count (int, optional): The maximum number of matches to find. Defaults to None.

    Returns:
    - results (Dict[str, List[int]]): A dictionary where keys are substrings, and values are lists of starting positions
     of matches in the input string.
    """
    string_len = len(string)
    results = {}
    j = {}
    prefix = {}
    exit_flag = {}
    i = {}
    c = 0
    exit_flag_count = False

    for substring in substrings:
        results[substring] = []
        j[substring] = 0
        i[substring] = 0
        exit_flag[substring] = False
        prefix[substring] = func_prefix(substring)

    while True:
        for substring in substrings:
            if i[substring] >= string_len:
                exit_flag[substring] = True
                continue
            substring_len = len(substring)
            if string[i[substring]] == substring[j[substring]]:
                if j[substring] == substring_len - 1:
                    results[substring].append(i[substring] - substring_len + 1)
                    c += 1
                    j[substring] = prefix[substring][j[substring]]

                    if count is not None and c >= count:
                        exit_flag_count = True
                        break
                else:
                    j[substring] += 1
                i[substring] += 1

            elif j[substring]:
                j[substring] = prefix[substring][j[substring] - 1]

            else:
                i[substring] += 1

        if all(value for value in exit_flag.values()):
            break

        if exit_flag_count:
            break
    return results


def func_prefix(substring: str) -> List[int]:
    """
    Compute the prefix function for a given substring.

    Args:
    - substring (str): The substring for which to compute the prefix function.

    Returns:
    - prefix (List[int]): The prefix function values for the given substring.

    This function computes the prefix function, which is used internally
     by the KMP algorithm to find matches efficiently.
    """
    substring_len = len(substring)
    prefix = [0] * substring_len
    i, j = 0, 1
    while j < substring_len:
        if substring[i] == substring[j]:
            prefix[j] = i + 1
            i += 1
            j += 1
        elif i:
            i = prefix[i - 1]
        else:
            prefix[j] = 0
            j += 1
    return prefix


def kmp_reverse(string: str, substrings: List[str], count: Optional[int] = None) -> Dict[str, List[int]]:
    """
    Search for substrings in a given string from the end using the Knuth-Morris-Pratt (KMP) algorithm.
    
    Args:
    - string (str): The input string to search within, in reverse order.
    - substrings (List[str]): A list of reversed substrings to search for in the reversed input string.
    - count (int, optional): The maximum number of matches to find. Defaults to None.
    
    Returns:
    - results (Dict[str, List[int]]): A dictionary where keys are substrings,
    and values are lists of starting positions of matches in the reversed input string.
    """
    string = string[::-1]
    results = {}
    i = {}
    j = {}
    prefix = {}
    exit_flag = {}
    c = 0
    exit_flag_count = False

    for substring in substrings:
        results[substring] = []
        j[substring] = 0
        i[substring] = 0
        exit_flag[substring] = False
        prefix[substring] = func_prefix(substring[::-1])

    while True:
        for substring in substrings:
            if i[substring] == len(string):
                exit_flag[substring] = True
                continue

            substring_len = len(substring)
            reversed_substring = substring[::-1]

            if string[i[substring]] == reversed_substring[j[substring]]:
                if j[substring] == substring_len - 1:
                    results[substring].append(i[substring] - substring_len + 1)
                    c += 1
                    j[substring] = prefix[substring][j[substring]]

                    if count is not None and c == count:
                        exit_flag_count = True
                        break
                else:
                    j[substring] += 1
                i[substring] += 1

            elif j[substring]:
                j[substring] = prefix[substring][j[substring] - 1]

            else:
                i[substring] += 1

        if all(value for value in exit_flag.values()):
            break

        if exit_flag_count:
            break

    for substring in substrings:
        results[substring] = [len(string) - x - len(substring) for x in results[substring]]
    return results
