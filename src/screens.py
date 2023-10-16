import xml.etree.ElementTree as ET

# Local modules
from .paths import XML_PATH
from .write import write


TEXT_TAG = "text"
OPTION_TAG = "option"

tree = ET.parse(XML_PATH)
root = tree.getroot()
option_lines = []


def get_screen_element(id: int) -> ET.Element:
    """
    Returns the screen `Element` with a given `id` attribute.
    """
    screen_element = root.find(f".screens//screen[@id='{id}']")
    
    if screen_element is None:
        raise Exception(f"No screen with ID {id}.")
    
    return screen_element


def get_screen_text(id: int) -> str:
    """
    Returns a given screen's full text string, ready to be printed.
    """
    screen = get_screen_element(id)
    screen_text = ""

    elements = screen.findall(".*")
    num_elements = len(elements)

    for index, elem in enumerate(elements):
        if elem.tag == TEXT_TAG:
            screen_text += elem.text # type: ignore
        else:
            screen_text += f"[{elem.text}]"

        if index < num_elements - 1:
            screen_text += "\n\n"

    return screen_text


def render_screen(window, id: int) -> None:
    """
    Renders a screen's content based on a given ID.
    """
    """
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
   
    """   
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
   
    title_element = root.find("title")
    subtitle_element = root.find("subtitle")
    screen_text = get_screen_text(id)

    result_text = ""
    if title_element is not None and title_element.text:
        result_text += f"{title_element.text}\n"
    if subtitle_element is not None and subtitle_element.text:
        result_text += f"{subtitle_element.text}\n"
    if result_text:
        result_text += "\n"
    
    result_text += screen_text

    write(window, result_text)
    
