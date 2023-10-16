import xml.etree.ElementTree as ET

# Local modules
from .paths import XML_PATH
from .write import write


tree = ET.parse(XML_PATH)
root = tree.getroot()


def get_header() -> str:
    title_element = root.find("title")
    subtitle_element = root.find("subtitle")

    result_text = ""
    if title_element is not None and title_element.text:
        result_text += f"{title_element.text}\n"
    if subtitle_element is not None and subtitle_element.text:
        result_text += f"{subtitle_element.text}\n"
    if result_text:
        result_text += "\n"

    return result_text


def get_menu_element(id: int) -> ET.Element:
    """
    Returns the menu `Element` with a given `id` attribute.
    """
    menu_element = root.find(f".menus//menu[@id='{id}']")
    
    if menu_element is None:
        raise Exception(f"No menu with ID {id}.")
    
    return menu_element


def get_menu_notes_string(menu: ET.Element) -> str:
    """
    Returns a given menu's full notes string, ready to be printed.
    """
    menu_notes = ""

    paragraph_elements = menu.findall(".notes/p")

    for elem in paragraph_elements:
        menu_notes += f"{elem.text}\n" # type: ignore # consider adding "or '' to use empty string"

    return menu_notes


def get_menu_options_string(menu: ET.Element) -> str:
    """
    Returns a given menu's full options string, ready to be printed.
    """
    menu_options = ""

    option_elements = menu.findall(".options/option")
    
    for elem in option_elements:
        menu_options += f"[{elem.text}]\n"

    return menu_options


def render_menu(window, id: int) -> None:
    """
    Renders a menu's content based on a given ID.
    """
    header = get_header()

    menu = get_menu_element(id)
    menu_notes = get_menu_notes_string(menu)
    menu_options = get_menu_options_string(menu)

    if menu_notes and menu_options:
        menu_notes += "\n"
    
    result_text = header + menu_notes + menu_options

    write(window, result_text)
    