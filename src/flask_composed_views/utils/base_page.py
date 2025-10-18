from ..components import BaseComponent, PlainText, BaseTag
class BasePage(BaseComponent):
    def __init__(self,
                 title: str = "",
                 stylesheets: list[str] | None = None,
                 scripts: list[str] | None = None,
                 scripts_defer: bool = True,
                 metas: list[dict] | None = None,
                 children=None):
        """Beware: stylesheets, scripts and metas are neither checked for injection, nor escaped.
        """
        self.title = PlainText(title)
        self.stylesheets = stylesheets
        self.scripts = scripts
        self.metas = metas
        self.scripts_defer = scripts_defer
        if(children is None):
            children = []
        elif(not isinstance(children, list)):
            children = [ children, ]
        super().__init__(children=children)

    def _build_meta(self, meta_dict: dict) -> str:
        return ' '.join([ '<meta', ] + [ f'{name}="{value}"' for name, value in meta_dict.items() ] + [ '>', ])

    def _build_header(self) -> str:
        header = '<head>\n<meta charset="UTF-8">\n'
        header += BaseTag('title', children=self.title).render() + '\n'
        if(self.metas):
            header += '\n'.join([
                        self._build_meta(meta)
                        for meta in self.metas
                       ]) + '\n'
        if(self.stylesheets):
            header += '\n'.join([
                        f'<link rel="stylesheet" href="{stylesheet_url}">'
                        for stylesheet_url in self.stylesheets
                       ]) + '\n'
        if(self.scripts):
            header += '\n'.join([
                            f'<script src="{script_url}" {"defer" if(self.scripts_defer) else ""}></script>\n'
                            for script_url in self.scripts
                        ]) + '\n'
        header += '</head>\n'
        return header
    
    def render(self) -> str:
        page_content = [
            f'<html>{self._build_header()}<body>', 
            super().render(),
            '\n</body></html>',
        ]
        return "".join(page_content)