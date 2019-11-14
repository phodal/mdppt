class TWLayout:
    def __init__(self, prs):
        self.slide_masters = prs

    def get_black_layout(self):
        return self.slide_masters[0].slide_layouts[0]

    def get_quote_layout(self):
        return self.slide_masters[0].slide_layouts[8]

    def get_list_layout(self):
        return self.slide_masters[0].slide_layouts[0]
