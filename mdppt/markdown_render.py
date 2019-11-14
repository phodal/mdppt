import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class SimpleSlideVO(object):
    def __init__(self):
        self.header = ''
        self.paragraph = ''
        super().__init__()


class MarkdownRender(mistune.Renderer):
    def __init__(self, **kwargs):
        self.md_slides = []
        self.current_slide = SimpleSlideVO()
        super().__init__(**kwargs)

    def header(self, text, level, raw=None):
        if self.current_slide.header != "":
            self.md_slides.append(self.current_slide)
            self.current_slide = SimpleSlideVO()

        self.current_slide.header = text
        return super().header(text, level, raw)

    def paragraph(self, text):
        self.current_slide.paragraph = text
        return super().paragraph(text)

    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                   mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

    def get_ppt_data(self):
        self.md_slides.append(self.current_slide)
        self.current_slide = SimpleSlideVO()
        return self.md_slides
