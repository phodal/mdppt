import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
import html as sysHtml


class SimpleSlideVO(object):
    def __init__(self):
        self.header = ''
        self.paragraph = []
        self.quote = ''
        self.title = ''
        self.code = ''
        self.lang = ''
        self.dot = ''
        self.image_src = ''
        self.list = []
        self.table = []
        self.header_level = 0
        super().__init__()


class MarkdownRender(mistune.Renderer):
    def __init__(self, **kwargs):
        self.md_slides = []
        self.slide_vo = SimpleSlideVO()
        self.table_header_size = 0
        self.current_table_cells_size = 0
        self.current_row = []
        self.had_append_header = False
        self.has_enter_table_body = False
        super().__init__(**kwargs)

    def header(self, text, level, raw=None):
        if self.slide_vo.header != "":
            self.md_slides.append(self.slide_vo)
            self.slide_vo = SimpleSlideVO()

        self.slide_vo.header_level = text
        self.slide_vo.header = sysHtml.unescape(text)
        return super().header(text, level, raw)

    def paragraph(self, text):
        self.slide_vo.paragraph.append(sysHtml.unescape(text))
        return super().paragraph(text)

    def block_code(self, code, lang=None):
        if lang == 'dot':
            self.slide_vo.dot = code
            return code
        else:
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

    def table_cell(self, content, **flags):
        if flags.get("header"):
            if self.has_enter_table_body:
                self.current_row = []
                self.slide_vo.table = []
                self.table_header_size = 0
                self.current_table_cells_size = 0

            self.current_row.append(content)
            self.table_header_size = self.table_header_size + 1
            self.has_enter_table_body = False
            self.had_append_header = False
        else:
            self.has_enter_table_body = True
            if not self.had_append_header:
                self.had_append_header = True
                self.slide_vo.table.append(self.current_row)
                self.current_row = []

            self.current_row.append(content)
            self.current_table_cells_size = self.current_table_cells_size + 1

            if self.current_table_cells_size == self.table_header_size:
                self.current_table_cells_size = 0
                self.slide_vo.table.append(self.current_row)
                self.current_row = []

        return ""

    def list_item(self, text):
        self.slide_vo.list.append(sysHtml.unescape(text))
        return super().list_item(text)

    def get_ppt_data(self):
        self.md_slides.append(self.slide_vo)
        self.slide_vo = SimpleSlideVO()
        return self.md_slides
