import json

# Local modules
from .paths import TERMINAL_PATH
from .write import write


with open(TERMINAL_PATH, 'r') as file:
    root = json.load(file)


def get_header() -> str:
    title_element = root['title']
    subtitle_element = root['subtitle']

    result_text = ""
    if title_element is not None:
        result_text += f"{title_element}\n"
    if subtitle_element is not None:
        result_text += f"{subtitle_element}\n"
    if result_text:
        result_text += "\n"

    return result_text


def get_menu(id: int):
    """
    Returns the menu `Element` with a given `id` attribute.
    """
    menu = root['menus'][str(id)]
    
    if menu is None:
        raise Exception(f"No menu with ID {id}.")
    
    return menu


def get_menu_notes_string(menu) -> str:
    """
    Returns a given menu's full notes string, ready to be printed.
    """
    notes_string = ""

    notes = menu['notes']

    for note in notes:
        notes_string += f"{note}\n" # type: ignore # consider adding "or '' to use empty string"

    return notes_string


def get_menu_options_string(menu) -> str:
    """
    Returns a given menu's full options string, ready to be printed.
    """
    options_string = ""

    options = menu['options']
    
    for option in options:
        options_string += f"[{option}]\n"

    return options_string


def render_menu(window, id: int) -> None:
    """
    Renders a menu's content based on a given ID.
    """

    menu = get_menu(id)

    header = get_header()
    menu_notes = get_menu_notes_string(menu)
    menu_options = get_menu_options_string(menu)

    if menu_notes and menu_options:
        menu_notes += "\n"
    
    result_text = header + menu_notes + menu_options

    write(window, result_text)
    