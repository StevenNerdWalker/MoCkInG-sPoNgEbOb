import random


def get_lower_alphabet():
    return {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'ô', 'ú', 'ç'}


def random_caps(input_string: str):
    """"Takes a string and returns a string with the characters randomly alternating between upper and lowercase."""
    input_string = input_string.lower()
    new_str = ''
    for char in input_string:
        char = random.choice([char, char.upper()])
        new_str += char

    return new_str


def alternating_caps(input_string: str, begin_lower: bool = True):
    """Takes a string and returns a string with the characters alternating between uppercase and lowercase, only taking letters into consideration, not other characters.
    If begin_lower is True, the first letter will be lowercase, the second uppercase, and so on.
    If begin_lower is False, the first letter will be uppercase and so on."""

    lower_alphabet = get_lower_alphabet()

    input_string = input_string.lower()
    new_str = ''
    even_letter = True

    for i in range(len(input_string)):
        char = input_string[i]

        if char not in lower_alphabet:
            new_str += char
            continue # dont update even_letter cause this wasnt a letter
        
        if even_letter: 
            if begin_lower: # even letters are lower
                new_str += char
            else:
                new_str += char.upper()
            even_letter = False

        else:   # odd letter
            if begin_lower: # odd letters are upper
                new_str += char.upper()
            else:
                new_str += char
            even_letter = True

    return new_str


def mocking_caps(input_string: str, max_equal_case: int = 3, only_count_letters: bool = True):
    """Takes a string and returns a string with the letters randomly varying between upper and lowercase while avoiding too many letters in a row with the same case.
    max_equal_case determines the maximum number of consecutive characters that are allowed to be in the same case, in order to feel more organic and random.
    only_count_letters determines if letters are the only characters considered for max_equal_case, or if it also counts spaces, commas, and other characters."""
    
    lower_alphabet = get_lower_alphabet()
    input_string = input_string.lower()
    new_str = ''
    new_str_only_letters = ''   # keep track of the new string but with only the letters to check if it hit the limit

    # loop through the characters
    for i in range(len(input_string)):
        char = input_string[i]

        # character isnt a letter
        if char not in lower_alphabet:
            new_str += char
            continue

        # set the string to be considered
        if only_count_letters:  # considering only letters, not all characters
            str_to_consider = new_str_only_letters
        else:                   # considering all characters
            str_to_consider = new_str

        if len(str_to_consider) >= max_equal_case:  # there are enough letters for there to be max_equal_case consecutive characters in the same case
            end_chars = str_to_consider[-max_equal_case:]

            if end_chars.lower() == end_chars:      # the last max_equal_case characters were all lowercase
                new_str += char.upper()
                new_str_only_letters += char.upper()

            elif end_chars.upper() == end_chars:    # the last max_equal_case characters were all uppercase
                new_str += char.lower()
                new_str_only_letters += char.lower()

            else:
                char = random.choice([char.lower(), char.upper()])
                new_str += char
                new_str_only_letters += char

        else:   # there arent enough letters
            char = random.choice([char.lower(), char.upper()])
            new_str += char
            new_str_only_letters += char

    return new_str

