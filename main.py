import os

from pptx import Presentation

from mdppt.markdown_render import SimpleSlideVO
from mdppt.md_parser import MDParser
from mdppt.md_slide import MdSlider

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run_markdown_ppt(slides_data):
    prs = get_presentations()
    prs.core_properties.title = "title"

    slider = MdSlider(prs)

    for content in slides_data:
        if content.header:
            slider.add_normal_slide(content.header, content.paragraph)
        if content.quote:
            slider.add_quote_slide("quote")

    prs.save('test.pptx')


def get_presentations():
    file_path = os.path.join(__location__, 'templates/tw-slides2.pptx')
    f = open(file_path, 'rb')
    prs = Presentation(f)
    f.close()
    return prs


if __name__ == "__main__":
    md_file = open(os.path.join(__location__, 'ppt.md'), 'r')
    content = md_file.read()
    md_parser = MDParser()
    result, slidesData = md_parser.render(content)
    run_markdown_ppt(slidesData)
