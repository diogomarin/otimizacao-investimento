import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ===== Layout ===== #
layout = dbc.Col([
            html.H1("Viabilidade Econômica", className="text-primary"),
            html.P("By Diogo Marin", className="text-info"),
            html.Hr(),

    # ---- SECAO DO PERFIL ---- #
            dbc.Button(id="botao_avatar",
                       children=[html.Img(src="/assets/img_business.png", id="avatar_change", alt="Avatar", className="perfil_avatar"),
            ], style={'background-color': 'transparent', 'border-color': 'transparent'}),

    # ---- SECAO DE CADASTRO ---- #
            dbc.Row([
                dbc.Col([
                    dbc.Button(color="secondary", id="open-novo-investimento",
                               children=["Investimento"]),
                ], width=6),

            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Button(color="success", id="open-novo-receita",
                               children=["Receita"],)
                ], width=3),

                dbc.Col([
                    dbc.Button(color="danger", id="open-novo-despesa",
                               children=["Despesa"],)
                ], width=3),

                dbc.Col([
                    dbc.Button(color="warning", id="open-novo-depreciacao",
                               children=["Depreciação"],)
                ], width=4),                

            ]),
        
        ])

            # --- Modal Investimento --- #



# ===== Callbacks ===== #
# Pop-up investimentos
# Pop-up receitas
# Pop-up despesas
# Pop-up depreciacoes