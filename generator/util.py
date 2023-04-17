import re
from typing import Set
import json
from catppuccin import Flavour


def pprint(d: dict) -> None:
    print(json.dumps(d, sort_keys=True, indent=4))


def __find_all_hex_codes_impl(file_name:str="DefaultDarkTheme.xml") -> Set[str]:
    hex_regex = re.compile(r'([a-zA-Z][a-zA-Z_]*)="#([0-9a-fA-F]{6})"') # var_name="#ABCDEF"
    hex_names = dict() # hex code -> set of names associated with it
    with open(file_name, 'r') as file:
        for line in file:
            matches = hex_regex.findall(line)
            for name, hex in matches:
                hex_names[hex] = hex_names.get(hex, set()).union({name})
    hex_names = { hexcode: list(names) for hexcode, names in hex_names.items() } # Turn into valid JSON
    return hex_names


def find_all_hex_codes(file_name:str="DefaultDarkTheme.xml") -> None:
    """
    Prints all colors used . This helps with creating
    the mappings between default theme colors to catppuccin theme colors
    """
    hex_names = __find_all_hex_codes_impl(file_name=file_name)
    pprint(hex_names)


def map_colors(input_file:str="DefaultDarkTheme.xml", opt={}, mapping={}, output_file_name:str="output.xml") -> None:
    """
    Replaces all instances of a color in input_file with a different color using the definition in mapping.
    """
    DUMMY_VALUE = "$$$"
    with open(input_file, 'r') as file:
        file_contents = file.read()
        for start_hex, end_value in mapping.items():
            if not isinstance(end_value, str):
                end_value = end_value(opt)
            file_contents = file_contents.replace(f'#{start_hex}', f'{DUMMY_VALUE}{end_value}')
        file_contents = file_contents.replace(DUMMY_VALUE, "#")
    with open(output_file_name, "w") as output_file:
        output_file.write(file_contents)