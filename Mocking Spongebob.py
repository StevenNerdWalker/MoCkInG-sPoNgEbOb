

def alternating_caps(input: str, begin_lower: bool = True) -> str:
    """Takes a string and returns a string with the characters alternating between uppercase and lowercase, only taking letters into consideration, not other characters.
    If begin_lower is True, the first letter will be lowercase, the second uppercase, and so on.
    If begin_lower is False, the first letter will be uppercase and so on."""

    lower_alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                      'á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'ô', 'ú'}

    input = input.lower()
    new_str = ''
    even_letter = True

    for i in range(len(input)):
        char = input[i]

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

print(alternating_caps('Mas isso vai confundir a cabeça das crianças!!1!'))
print(alternating_caps('a style in which you alternate between lowercase and uppercase letters to make fun of what someone has said and ridicularize them'))