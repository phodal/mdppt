import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class SimpleSlideVO(object):
    def __init__(self):
        self.header = ''
        self.paragraph = ''
        self.quote = ''
        self.title = ''
        self.code = ''
        self.lang = ''
        self.image_src = ''
        self.list = []
        super().__init__()


class MarkdownRender(mistune.Renderer):
    def __init__(self, **kwargs):
        self.md_slides = []
        self.slide_vo = SimpleSlideVO()
        super().__init__(**kwargs)

    def header(self, text, level, raw=None):
        if self.slide_vo.header != "":
            self.md_slides.append(self.slide_vo)
            self.slide_vo = SimpleSlideVO()

        self.slide_vo.header = text
        return super().header(text, level, raw)

    def paragraph(self, text):
        self.slide_vo.paragraph = text
        return super().paragraph(text)

    def block_code(self, code, lang=None):
        self.slide_vo.code = code
        self.slide_vo.lang = lang
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                   mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

    def block_quote(self, text):
        self.slide_vo.quote = text
        return ""

    def image(self, src, title, text):
        self.slide_vo.image_src = src
        # return super().image(src, title, text)
        return ""

    def list_item(self, text):
        self.slide_vo.list.append(text)
        return super().list_item(text)

    def get_ppt_data(self):
        self.md_slides.append(self.slide_vo)
        self.slide_vo = SimpleSlideVO()
        return self.md_slides
