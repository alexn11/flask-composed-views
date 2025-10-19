from flask_composed_views.components import List, ListItem, PlainText, Span

def test_list_base():
    list_element = List('unordered', id='my-list-an-id', classes=['class1','class2'],
                        list_items=[
                            PlainText('item 1'),
                            PlainText('item 2'),
                            PlainText('etc'),
                        ])
    rendered_list = list_element.render().replace('\n', '')
    assert(rendered_list == '<ul id="my-list-an-id" class="class1 class2"><li>item 1</li><li>item 2</li><li>etc</li></ul>')
    list_element = List('ordered', id='my-list-xx', classes=['classy'],
                        list_items=[
                            PlainText('item 3'),
                            PlainText('item 4'),
                            PlainText('etc 0'),
                        ])
    rendered_list = list_element.render().replace('\n', '')
    assert(rendered_list == '<ol id="my-list-xx" class="classy"><li>item 3</li><li>item 4</li><li>etc 0</li></ol>')

def test_list_custom_items():
    list_element = List('unordered',
                        list_items=[
                            PlainText('auto item'),
                        ],
                        children=[
                            ListItem(text='basic', id='item-id-0'),
                            ListItem(text='editable', other_attributes={'editablecontent': 'true'}),
                            ListItem(children=[Span('span-thing'),], id='item-id-1', classes=['cl-item']),
                        ])
    rendered_list = list_element.render().replace('\n', '')
    assert(rendered_list == '<ul><li id="item-id-0">basic</li><li editablecontent="true">editable</li><li id="item-id-1" class="cl-item"><span>span-thing</span></li><li>auto item</li></ul>')