class TWLayout:
    def __init__(self, prs):
        self.slide_masters = prs

    def get_layout_by_level(self, level):
        layout = self.slide_masters[0].slide_layouts[0]
        if level == 1:
            layout = self.slide_masters[0].slide_layouts[11]
        return layout

    def get_quote_layout(self):
        return self.slide_masters[0].slide_layouts[8]

    def get_list_layout(self):
        return self.slide_masters[0].slide_layouts[0]
