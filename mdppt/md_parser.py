import mistune

from mdppt.higlight_render import HighlightRenderer


class MDParser:
    def __init__(self):
        pass

    def render(self, text):
        renderer = HighlightRenderer()
        markdown = mistune.Markdown(renderer=renderer)
        compile_text = markdown(text)

        data = renderer.get_ppt_data()
        return compile_text, data
