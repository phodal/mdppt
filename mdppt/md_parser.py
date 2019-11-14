import mistune

from mdppt.markdown_render import MarkdownRender


class MDParser:
    def __init__(self):
        pass

    def render(self, text):
        renderer = MarkdownRender()
        markdown = mistune.Markdown(renderer=renderer)
        compile_text = markdown(text)

        data = renderer.get_ppt_data()
        return compile_text, data
