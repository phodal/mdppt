import os

import pydot

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class MDDot:
    def __init__(self) -> None:
        super().__init__()

    def build_graph(self, data, image_count):
        (graph,) = pydot.graph_from_dot_data(data)
        graph.write_png('images/dot' + image_count.__str__() + '.png')
