# cintel-02-data: Palmer Penguins Data Dashboard

## Overview
This project is a Python-based interactive web app that displays data from the Palmer Penguins dataset. It provides visualizations such as histograms and scatterplots using Plotly and Seaborn libraries, along with data tables and grids. The app allows users to select attributes, species, and adjust histogram bin counts interactively through a sidebar.

## Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/dgraves4/cintel-02-data.git
    ```

2. Navigate to the project directory:
    ```bash
    cd cintel-02-data
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the `app.py` file to start the web app:
    ```bash
    python app.py
    ```
    
2. Use the sidebar to select attributes, species, and adjust bin counts. Explore the different visualizations and data tables provided.

## Requirements
- Python 3.6+
- plotly
- shiny
- shinywidgets
- palmerpenguins
- seaborn
- pandas

## Files
- `app.py`: Python code for the web app.
- `requirements.txt`: List of Python dependencies required to run the app.

## Acknowledgements
- The Palmer Penguins dataset is provided by [palmerpenguins](https://github.com/allisonhorst/palmerpenguins).
- Shiny is a Python library for building interactive web apps, used in this project.
- Plotly and Seaborn are used for data visualization.
