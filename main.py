import os

from pptx import Presentation
from pygments import highlight
from pygments.lexers import PythonLexer

from pygments.formatters import SvgFormatter

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run_markdown_ppt():
    prs = get_presentations()
    add_slides(prs, "REPORT", "REPORT 1")

    prs.save('test.pptx')


def add_slides(prs, title_text, content_text):
    slide = prs.slides.add_slide(prs.slide_masters[0].slide_layouts[0])
    title = slide.placeholders[0]
    title.text = title_text
    sub_title = slide.placeholders[1]
    sub_title.text = content_text

    code = 'print "Hello World"'
    values = highlight(code, PythonLexer(), SvgFormatter(noclasses=True))
    print(values)


def get_presentations():
    file_path = os.path.join(__location__, 'templates/tw-slides2.pptx')
    f = open(file_path, 'rb')
    prs = Presentation(f)
    f.close()
    return prs


if __name__ == "__main__":
    run_markdown_ppt()
