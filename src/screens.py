import xml.etree.ElementTree as ET

# Local modules
from .paths import XML_PATH
from .write import write


TEXT_TAG = "text"
OPTION_TAG = "option"


def getScreenElement(id: int) -> ET.Element:
    """
    Returns the screen `Element` with a given `id` attribute.
    """
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
    screenElement = root.find(f".screens//screen[@id='{id}']")
    
    if screenElement is None:
        raise Exception(f"No screen with ID {id}.")
    
    return screenElement


def getScreenText(id: int) -> str:
    """
    Returns a given screen's full text string, ready to be printed.
    """
    screen = getScreenElement(id)
    screenText = ""

    elements = screen.findall(".*")
    num_elements = len(elements)

    for index, elem in enumerate(elements):
        if elem.tag == TEXT_TAG:
            screenText += elem.text # type: ignore
        else:
            screenText += f"[{elem.text}]"

        if index < num_elements - 1:
            screenText += "\n\n"

    return screenText


def renderScreen(window, id: int) -> None:
    """
    Renders a screen's content based on a given ID.
    """
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
   
    title_element = root.find("title")
    subtitle_element = root.find("subtitle")
    screen_text = getScreenText(id)

    result_text = ""
    if title_element is not None and title_element.text:
        result_text += f"{title_element.text}\n"
    if subtitle_element is not None and subtitle_element.text:
        result_text += f"{subtitle_element.text}\n"
    if result_text:
        result_text += "\n"
    
    result_text += screen_text

    write(window, result_text)
