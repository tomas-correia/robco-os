import xml.etree.ElementTree as ET

# Local modules
from .paths import SCREENS_PATH


TEXT_TAG = "text"
OPTION_TAG = "option"


def getScreenElement(idToFetch) -> ET.Element:
    """
    Returns the `Element` with a given `id` attribute.
    """
    tree = ET.parse(SCREENS_PATH)
    root = tree.getroot()
    xpath_expression = f".screen[@id='{idToFetch}']"
    result = root.find(xpath_expression)
    
    if result is None:
        raise Exception("Missing <struct> node in screen XML definition")
    
    return result


def getScreenText(id) -> str:
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
