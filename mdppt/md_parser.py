import mistune

from mdppt.higlight_render import HighlightRenderer


class MDParser:
    def __init__(self):
        pass

    def render(self, text):
        renderer = HighlightRenderer()
        markdown = mistune.Markdown(renderer=renderer)
        return markdown(text)
