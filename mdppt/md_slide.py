from mdppt.layout import TWLayout


class MdSlide:
    def __init__(self, prs) -> None:
        self.tw_layout = TWLayout(prs.slide_masters)
        super().__init__()

    def add_quote(self):
        layout = self.tw_layout.get_quote_layout()