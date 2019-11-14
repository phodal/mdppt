import os

from pptx import Presentation

from mdppt.md_parser import MDParser
from mdppt.md_slide import MdSlider

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run_markdown_ppt():
    prs = get_presentations()
    prs.core_properties.title = "title"

    slider = MdSlider(prs)
    slider.add_normal_slide("text", "content")
    slider.add_quote_slide("quote")

    prs.save('test.pptx')


def get_presentations():
    file_path = os.path.join(__location__, 'templates/tw-slides2.pptx')
    f = open(file_path, 'rb')
    prs = Presentation(f)
    f.close()
    return prs


if __name__ == "__main__":
    md_parser = MDParser()
    result, data = md_parser.render("# h1 \n ## h2 \n ")
    print(result, data)
    run_markdown_ppt()
