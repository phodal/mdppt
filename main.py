import os

from pptx import Presentation

from mdppt.md_parser import MDParser
from mdppt.md_slide import MdSlider

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run_markdown_ppt(content_list):
    prs = get_presentations()
    prs.core_properties.title = "title"

    slider = MdSlider(prs)

    for content in content_list:
        current_slide = None
        print(content.table)

        if content.quote:
            slider.add_quote_slide(content.paragraph)
            continue

        if content.list:
            slider.add_list_slide(content.header, content.list)
            continue

        if content.header:
            current_slide = slider.add_normal_slide(content.header, content.paragraph)

        if content.code and current_slide:
            slider.add_code(content.code, "right")

        if content.dot and current_slide:
            slider.add_dot(content.dot, "right")

        if content.image_src and current_slide:
            slider.add_image(content.image_src, "right")

    prs.save('test.pptx')


def get_presentations():
    file_path = os.path.join(__location__, 'templates/default.pptx')
    f = open(file_path, 'rb')
    prs = Presentation(f)
    f.close()
    return prs


if __name__ == "__main__":
    md_file = open(os.path.join(__location__, 'ppt.md'), 'r')
    result, slidesData = MDParser().render(md_file.read())
    run_markdown_ppt(slidesData)
