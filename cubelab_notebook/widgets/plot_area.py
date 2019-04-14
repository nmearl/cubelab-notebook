from ipywidgets import VBox
import plotly.graph_objs as go
import plotly.plotly as py
import numpy as np


class PlotArea(VBox):
    def __init__(self, **kwargs):
        random_x = np.random.randn(1000)
        random_y = np.random.randn(1000)

        self._trace = go.Scatter(
            x=random_x,
            y=random_y,
            mode='markers'
        )

        self._figure = go.FigureWidget(
            data=[self._trace],
            layout=go.Layout(barmode='overlay'))

        super().__init__(children=[self._figure], **kwargs)