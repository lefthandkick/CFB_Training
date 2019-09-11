"""
Create proram to will lookup work in a dictionary, and display
the work's definition.
- Use types / mypy
- No classes only functions
- Pass aguments
- Demonstrate fuction channing ie? xxx.yyy()
- Write tests
- CLI for user input
- Allow for proper names (fist letter Cap)
- Make Suggestions if work not found
- Make the output look good/formatted
- Use try/except for managing error situations

Follow After Success
- Refactor using Class approach
"""

# Libraries / Imports needed
from typing import TextIO, Dict, List
import json
import pathlib as pl
import difflib as df

# Constant Globals
EXIT: str = "zzz"
DICTIONARY = "dictionary.json"
# DICTIONARY = "_dictionary.json"

# Data - Dictionary in JSON format
def open_dictionary(dict_name: str) -> TextIO:
    json_dict: TextIO = None

    if pl.Path(dict_name).exists():
        json_dict = open(dict_name, "r")
        # print(f"<S> Dictinary ${dict_name} open: ")
    else:
        # print("<E> Not a Valid Dictionay - Filename: ")
        pass

    return json_dict


def read_dictionary(dict_on_disk: str) -> Dict:
    j_dict: Dict = dict()

    try:
        j_dict = json.loads(open_dictionary(dict_on_disk).read())
    except AttributeError as err:
        print(f"<E> Error ${err}")
        print(f"<E> Please provide correct dictionary Filename:")
    finally:
        print("Try-Excption Complete")

    return j_dict


def find_word(dictionry: Dict, word: str) -> List:
    # allow for propor nouns just skip the first letter
    # using this saves from if -> word.title()
    return dictionry[word[0] + word[1:].lower()]


def main():
    dictionary: Dict = None
    word_to_define: str = ""
    ifAlt: List = list()

    dictionary = read_dictionary(DICTIONARY)

    if dictionary:
        print(f"Dictionary contains: {len(dictionary)} words. \n")
    else:
        return

    while True:
        word_to_define = input("Enter a word to look up > ")

        if (word_to_define == EXIT):
            print("\nAll done thank you :) \n")
            return

        try:
            # [print(" - " + definition) for definition in find_word(dictionary, word_to_define)]
            [print(f" - {definition}")
             for definition in find_word(dictionary, word_to_define)]

            print("\n")

        except KeyError as err:
            print(f"\n -> {err} : Was not found in the dictionary \n")

            ifAlt = df.get_close_matches(word_to_define, dictionary)
            if len(ifAlt) > 0:
                print(f"What atbout? > {' | '.join(ifAlt)} \n")
            else:
                print(f"Word not found :\n")


main()
