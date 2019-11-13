import os

from pptx import Presentation
from pptx.util import Inches
from pygments import highlight
from pygments.formatters.img import ImageFormatter
from pygments.lexers.python import PythonLexer

from mdppt.md_parser import MDParser

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run_markdown_ppt():
    prs = get_presentations()
    add_slides(prs, "REPORT", "REPORT 1")

    prs.save('test.pptx')


def write_image_to_file(values, code=None):
    image_dir = os.path.join(__location__, 'images')
    if not os.path.exists(image_dir):
        os.mkdir(image_dir, 0o755)

    fo = open(os.path.join(__location__, 'images/code' + code.__str__() + '.png'), 'wb')
    fo.write(values)
    fo.close()


def add_slides(prs, title_text, content_text, code_count=1):
    slide = prs.slides.add_slide(prs.slide_masters[0].slide_layouts[0])
    title = slide.placeholders[0]
    title.text = title_text
    sub_title = slide.placeholders[1]
    sub_title.text = content_text

    code = 'print "Hello World" \nprint "Hello MdPpt"'
    values = build_code_image(code)
    write_image_to_file(values, code_count)

    left = top = Inches(4)
    pic = slide.shapes.add_picture(os.path.join(__location__, 'images/code' + code_count.__str__() + '.png'), left, top)


def build_code_image(code):
    return highlight(code, PythonLexer(), ImageFormatter(noclasses=True,
                                                         image_format='bmp',
                                                         image_pad='32',
                                                         line_number_bg='#fff',
                                                         line_number_fg='#fff',
                                                         font_size='64',
                                                         font_name='Inconsolata Bold for Powerline'))


def get_presentations():
    file_path = os.path.join(__location__, 'templates/tw-slides2.pptx')
    f = open(file_path, 'rb')
    prs = Presentation(f)
    f.close()
    return prs


if __name__ == "__main__":
    md_parser = MDParser()
    result = md_parser.render("# h1 \n ## h2 \n ")
    print(result)
    run_markdown_ppt()
