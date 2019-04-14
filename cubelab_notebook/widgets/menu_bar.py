from ipywidgets import HBox, Text, Button, Layout, ToggleButtons


class MenuBar(HBox):
    def __init__(self, **kwargs):
        self._load_textfield = Text(
            description="File Path",
            disabled=False)

        self._load_button = Button(
            description="Load",
            disabled=False,
            layout=Layout(width='100px'))

        self._view_mode_buttons = ToggleButtons(
            options=['1D', '2D', '3D'],
            description="View Mode",
            disabled=False,
            style={'button_width': '50px'}
        )

        super().__init__(children=[self._load_textfield, self._load_button, self._view_mode_buttons], **kwargs)

    def setup_connections(self):
        self._load_button.on_click(self._load_data_file)

    def _load_data_file(self):
        # The the data file path from the input text field