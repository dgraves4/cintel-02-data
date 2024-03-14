import plotly.express as px
from shiny.express import input, render, ui
from shinywidgets import render_plotly
from palmerpenguins import load_penguins
import seaborn as sns
import pandas as pd

penguins_df = load_penguins()

ui.page_opts(title="Penguin Data with Dgraves4", fillable=True)
with ui.sidebar(open="open"):
    ui.h2("Sidebar")
    ui.input_selectize(
        "selected_attribute",
        "Select Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )
    ui.input_numeric("plotly_bin_count", "Plotly Bin Count", 30)
    ui.input_slider(
        "seaborn_bin_count",
        "Seaborn Bin Count",
        1,
        100,
        30,
    )
    ui.input_checkbox_group(
        "selected_species_list",
        "Select Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie"],
        inline=True,
    )
    ui.hr()
    ui.a(
        "Dgraves4 on GitHub",
        href="https://github.com/dgraves4/cintel-02-data",
        target="_blank",
    )

with ui.layout_columns():
    with ui.card():
        ui.card_header("Data Table")

        @render.data_frame
        def penguin_datatable():
            return render.DataTable(penguins_df)

    with ui.card():
        ui.card_header("Data Grid")

        @render.data_frame
        def penguin_datagrid():
            return render.DataGrid(penguins_df)

with ui.layout_columns():
    with ui.card():
        ui.card_header("Plotly Histogram")

        @render_plotly
        def plotly_histogram():
            plotly_hist = px.histogram(
                data_frame=penguins_df,
                x=input.selected_attribute(),
                nbins=input.plotly_bin_count(),
                color="species",
            ).update_layout(
                title="Plotly Penguins Data by Attribute",
                xaxis_title="Selected Attribute",
                yaxis_title="Count",
            )
            return plotly_hist

    with ui.card():
        ui.card_header("Seaborn Histogram")

        @render.plot
        def seaborn_histogram():
            seaborn_hist = sns.histplot(
                data=penguins_df,
                x=input.selected_attribute(),
                bins=input.seaborn_bin_count(),
            )
            seaborn_hist.set_title("Seaborn Penguin Data by Attribute")
            seaborn_hist.set_xlabel("Selected Attribute")
            seaborn_hist.set_ylabel("Count")

    with ui.card():
        ui.card_header("Plotly Scatterplot")

        @render_plotly
        def plotly_scatterplot():
            plotly_scatter = px.scatter(
                penguins_df,
                x="bill_length_mm",
                y="bill_depth_mm",
                color="species",
                size_max=8,
                title="Plotly Scatterplot: Bill Depth and Length",
                labels={
                    "bill_depth_mm": "Bill Depth (mm)",
                    "bill_length_mm": "Bill Length(mm)",
                },
            )
            return plotly_scatter
