from ipywidgets import Button, GridBox, Layout, ButtonStyle, HBox, Accordion, VBox, IntSlider, Text, ToggleButtons
import numpy as np
from traitlets import Unicode


from .widgets.menu_bar import MenuBar
from .widgets.plot_area import PlotArea


class Application(GridBox):

    def __init__(self, *args, **kwargs):
        self._plot_area = PlotArea(description="Plot Area",
                                   layout=Layout(width='auto', grid_area='plot_area'))
        self._menu_bar = MenuBar(description="Menu Bar",
                                 layout=Layout(width='auto', grid_area='menu_bar'))
        self._side_bar = Button(description="Side Bar",
                                layout=Layout(widget='auto', grid_area='side_bar'))
        self._footer = Button(description="Footer",
                              layout=Layout(width='auto', grid_area='footer'))

        self._layout = Layout(
            width='100%',
            grid_template_rows='auto auto auto',
            grid_template_columns='25% 25% 25% 25%',
            grid_template_areas='''
            "menu_bar menu_bar menu_bar menu_bar"
            "plot_area plot_area plot_area plot_area"
            "footer footer footer footer"
            '''
        )

        super(Application, self).__init__(children=[self._menu_bar, self._plot_area, self._side_bar, self._footer],
                                          layout=self._layout, **kwargs)
