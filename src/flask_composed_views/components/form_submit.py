from .base_tag import BaseTag
from .base_component import BaseComponent
from .plain_text import PlainText

class FormSubmit(BaseTag):
    def __init__(self, label: BaseComponent | str, id = None, classes = None,):
        if(isinstance(label, str)):
            label = PlainText(label)
        super().__init__(tag='button',
                         id=id,
                         classes=classes,
                         other_attributes = {
                             'type': 'submit',
                         },
                         children = [ label, ])

