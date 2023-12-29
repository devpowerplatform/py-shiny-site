# FIXME: Rewrite as an Express app
from shiny import App, render, ui
from shiny.types import ImgData
from pathlib import Path
here = Path(__file__).parent

app_ui = ui.page_fluid(
    ui.input_checkbox("show", "Show image?", value = True),
    ui.output_image("image") #<<
)

def server(input, output, session):
    @render.image #<<
    def image():
        img = {"src": here/"shiny.png", "width": "100px"} #<<
        return img if input.show() else None

app = App(app_ui, server)
