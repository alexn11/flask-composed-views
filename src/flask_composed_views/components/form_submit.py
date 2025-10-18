from .base_tag import BaseTag
from .base_component import BaseComponent
from .plain_text import PlainText

class FormSubmit(BaseTag):
    def __init__(self, label: BaseComponent | str, id = None, classes = None, **other_attributes):
        if(isinstance(label, str)):
            label = PlainText(label)
        if(other_attributes is not None):
            other_attributes = other_attributes.copy()
        else:
            other_attributes = {}
        other_attributes['type'] = 'submit'
        super().__init__(tag='button',
                         id=id,
                         classes=classes,
                         other_attributes = other_attributes,
                         children = [ label, ])

