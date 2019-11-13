class TWLayout:
    def __init__(self, prs):
        self.slide_masters = prs

    def get_black_layout(self):
        return self.slide_masters[0].slide_layouts[0]
