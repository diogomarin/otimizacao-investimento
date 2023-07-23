from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *

# ===== LAYOUT ====== #
content = html.Div(id="page-content")


app.layout = dbc.Container(chilren=[


], fluid=True,)


if __name__ == '__main__':
    app.run_server(port=8051,  debug=True)