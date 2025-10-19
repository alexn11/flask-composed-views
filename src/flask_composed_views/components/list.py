from .base_tag import BaseTag
from .base_component import BaseComponent
from .plain_text import PlainText
from ..core.plain_text_utils import prepend_child

class ListItem(BaseTag):
    def __init__(self, text: str | None = None, children = None, id = None, classes = None, other_attributes = None):
        if(text is not None):
            children = prepend_child(PlainText(text), children)
        super().__init__('li', children, id, classes, other_attributes)

class OrderedListTag(BaseTag):
    def __init__(self, children = None, id = None, classes = None, other_attributes = None):
        super().__init__('ol', children, id, classes, other_attributes)

class UnorderedListTag(BaseTag):
    def __init__(self, children = None, id = None, classes = None, other_attributes = None):
        super().__init__('ul', children, id, classes, other_attributes)

class List(BaseComponent):
    def __init__(self,
                 list_type: str = 'ul',
                 id = None,
                 classes = None,
                 list_items: list[BaseComponent] | None = None,
                 children: list[BaseComponent] | None = None,
                 other_attributes: list | None = None):

        list_type = list_type.lower()
        if(list_items is None):
            list_items = []
        if(children is None):
            children = []

        if(list_type in ['ul', 'unordered']):
            list_class = UnorderedListTag
        elif(list_type in ['ol', 'ordered']):
            list_class = OrderedListTag
        else:
            raise ValueError(f'unknown list type: "{list_type}"')

        list_children = children + [ ListItem(children=[item]) for item in list_items ]
        full_list = list_class(children=list_children,
                               id=id,
                               classes=classes,
                               other_attributes=other_attributes)
        super().__init__(id=id, classes=classes, children=full_list)


