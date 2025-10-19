from .base_tag import BaseTag
from .plain_text import PlainText
from ..core.plain_text_utils import prepend_child

class Button(BaseTag):
    def __init__(self,
                 text: str | None = None,
                 name: str | None = None,
                 button_type: str | None = None,
                 id = None, classes = None, children = None,
                 **other_attributes):
        if(text is not None):
            children = prepend_child(PlainText(text), children)
        if(name is not None):
            other_attributes['name'] = name
        if(button_type is not None):
            other_attributes['type'] = button_type
        super().__init__(tag='button', id=id, classes=classes, children=children, other_attributes=other_attributes)
    