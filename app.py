import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins # Package to import penguin dataset

# Load dataset into DataFrame
penguins_df = palmerpenguins.load_penguins() 

ui.page_opts(title="Penguin Data with Dgraves", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
