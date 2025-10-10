from ..components.plain_text import PlainText

def prepend_child(child, children: list | None) -> list:
    return [ child, ] if children is None else children.insert(0, child)

def prepend_text(text: str | None = None,
                 children: list | None = None) -> list | None:
    if(text is None):
        return children
    return prepend_child(PlainText(text), children)