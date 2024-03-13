"""
search_utility Module
"""
import argparse

from colorama import Fore, Style

from search import search
from timing_decorator import timing_decorator


@timing_decorator
def main() -> None:
    """
     A command-line utility for searching substrings in a source string or file and highlighting matches.

    This utility allows you to search for one or more substrings in a source string or a text file and
    highlight the matches in the output. You can control case sensitivity, search method, and limit the
    number of matches to find.
    """
    parser = argparse.ArgumentParser(description="Substring Search Utility")
    parser.add_argument(
        "source",
        help="The input string or file path where substrings will be searched",
    )
    parser.add_argument("sub_string", nargs="+", help="Substrings to search for")
    parser.add_argument(
        "-s", "--case-sensitive",
        action="store_true",
        help="Perform case-sensitive search (default is case-insensitive)",
    )
    parser.add_argument(
        "-m", "--method",
        choices=["first", "last"],
        default="first",
        help="Search method (default: first)",
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        help="Maximum number of matches to find (default: unlimited)",
    )

    args = parser.parse_args()

    source = args.source
    sub_strings = tuple(args.sub_string)
    case_sensitivity = not args.case_sensitive
    method = args.method
    count = args.count

    # Check if the source is a file
    if source.endswith(".txt"):
        with open(source, "r", encoding="utf-8") as file:
            string = file.read()
    else:
        string = source

    results = search(string, sub_strings, case_sensitivity, method, count)

    if results is None:
        print("No matches found.")
    else:
        print("Search Results:")
        if len(sub_strings) == 1:
            color = Fore.GREEN
            start = 0

            if method == "last":
                results = results[::-1]
            highlighted_text = ""

            for result in results:
                end = result
                highlighted_text += string[start:end] + color + string[end:end + len(sub_strings[0])] + Style.RESET_ALL
                start = end + len(sub_strings[0])

            highlighted_text += string[start:]
            count = 0

            for i, char in enumerate(highlighted_text):
                if char == '\n':
                    count += 1
                    if count == 10:
                        highlighted_text = highlighted_text[:i]
                        break

            print(f"Found '{sub_strings[0]}' at position {results}:")
            print(highlighted_text)
            print()
        else:
            for sub_string in sub_strings:
                positions = results.get(sub_string)

                if positions:
                    color = Fore.GREEN

                    if method == "last":
                        positions = positions[::-1]
                    start = 0
                    highlighted_text = ""

                    for position in positions:
                        end = position
                        highlighted_text += string[start:end] + color + string[
                                                                        end:end + len(sub_string)] + Style.RESET_ALL
                        start = end + len(sub_string)

                    highlighted_text += string[start:]
                    count = 0

                    for i, char in enumerate(highlighted_text):
                        if char == '\n':
                            count += 1
                            if count == 10:
                                highlighted_text = highlighted_text[:i]
                                break

                    print(f"Found '{sub_string}' at position {results.get(sub_string)}:")
                    print(highlighted_text)
                    print()

                else:
                    print(f"No matches found for '{sub_string}'")


if __name__ == "__main__":
    main()
