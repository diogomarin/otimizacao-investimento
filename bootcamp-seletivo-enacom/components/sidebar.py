import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd

from app import app
#from globals import *

df_categorias = pd.read_csv("df_categorias.csv", index_col=0)
categorias = df_categorias.values.tolist()

df_prioridades = pd.read_csv("df_prioridades.csv", index_col=0)
prioridades = df_prioridades.values.tolist()

# ===== Layout ===== #
layout = dbc.Col([
                html.H1("Viabilidade Econômica", className="text-primary"),
                html.P("By Diogo Marin", className="text-info"),
                html.Hr(),

            # ---- SECAO DO PERFIL ---- #
                dbc.Button(id="botao_avatar",
                        children=[html.Img(src="/assets/img_business.png", id="avatar_change", alt="Avatar", className="perfil_avatar")],
                        style={'background-color': 'transparent', 'border-color': 'transparent'}),

            # ---- SECAO DE CADASTRO ---- #
                html.Div([
                dbc.Row([
                    dbc.Button("Cadastre o Investimento", color="secondary", id="open_novo_investimento"),
                    ]),

                # --- MODAL INVESTIMENTO --- #
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Adicione uma opção de investimento")),
                    
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Descrição: "),
                                dbc.Input(placeholder="Ex.: Aquisição de empresa concorrente", id= "txt_investimento"),
                            ], width=6),

                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.Label("Categoria: "),
                                dbc.Select(id="select_categoria", options=[{"label": i, "value": i} for i in categorias], value=categorias[0])
                            ], width=4),

                            dbc.Col([
                                html.Label("Prioridade: "),
                                dbc.Select(id="select_prioridade", options=[{"label": i, "value": i} for i in prioridades], value=prioridades[0])
                            ], width=4),

                        ]),
                    ]),
                    
                    dbc.ModalFooter([
                        dbc.Button("Adicionar Investimento", id="salvar_investimento", color="error"),
                        dbc.Popover(dbc.PopoverBody("Investimento Salvo"), target="salvar_investimento", placement="left", trigger="click"),
                    ]),
                ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal_novo_investimento",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True),
                
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.Button(color="success", id="open_novo_receita",
                                children=["Receita"]),
                    ], width=6),

                    dbc.Col([
                        dbc.Button(color="danger", id="open_novo_despesa",
                                children=["Despesa"]),
                    ], width=6),             

                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.Button(color="warning", id="open_novo_depreciacao",
                            children=["Depreciação"]),
                        ], width=6),                

                ]),

            ], id="sidebar_completa"
        )


# ===== Callbacks ===== #
# Pop-up investimentos
@app.callback(
    Output("modal_novo_investimento", "is_open"),
    Input("open_novo_investimento", "n_clicks"),
    State("modal_novo_investimento", "is_open"),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open



# Pop-up receitas
# Pop-up despesas
# Pop-up depreciacoes