from config import get_config


def get_slide_index_by_config(key):
    return int(get_config(key))


class TWLayout:
    def __init__(self, prs):
        self.group_index = int(get_slide_index_by_config("group"))
        self.slide_masters = prs

    def get_layout_by_level(self, level):
        h2_index = get_slide_index_by_config("h2")
        layout = self.slide_masters[self.group_index].slide_layouts[h2_index]
        if level == 1:
            h1_index = get_slide_index_by_config("h1")
            layout = self.slide_masters[self.group_index].slide_layouts[h1_index]
        return layout

    def get_quote_layout(self):
        quote_index = get_slide_index_by_config("quote")
        return self.slide_masters[self.group_index].slide_layouts[quote_index]

    def get_list_layout(self):
        list_index = get_slide_index_by_config("list")
        return self.slide_masters[self.group_index].slide_layouts[list_index]
