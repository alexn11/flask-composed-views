from .base_tag import BaseTag
from .form_hidden_input import FormHiddenInput

class Form(BaseTag):
    def __init__(self, id = None, classes = None, children=None,
                 method='POST', action: str = None,
                 csrf_token: str | None = None,
                 other_attributes: dict | None = None):
        if(children is None):
            children = []
        if(csrf_token):
            children.append(
                FormHiddenInput(other_attributes={
                                    'name': 'csrf_token',
                                    'value': csrf_token,
                                }))
        if(other_attributes is None):
            other_attributes = {}
        else:
            other_attributes = other_attributes.copy()
        other_attributes['method'] = method
        other_attributes['action'] = action if(action) else ''
        super().__init__(tag='form',
                         id=id,
                         classes=classes,
                         children=children,
                         other_attributes=other_attributes,)




