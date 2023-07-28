import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd

from app import app
from datetime import datetime, date
#from globals import *

df_categorias = pd.read_csv("df_categorias.csv", index_col=0)
categorias = df_categorias.values.tolist()

df_prioridades = pd.read_csv("df_prioridades.csv", index_col=0)
prioridades = df_prioridades.values.tolist()

df_classificacao_receita = pd.read_csv("df_classificacao_receita.csv", index_col=0)
classificacao_receita = df_classificacao_receita.values.tolist()

df_classificacao_despesa = pd.read_csv("df_classificacao_despesa.csv", index_col=0)
classificacao_despesa = df_classificacao_despesa.values.tolist()

df_classificacao_depreciacao = pd.read_csv("df_classificacao_depreciacao.csv", index_col=0)
classificacao_depreciacao = df_classificacao_depreciacao.values.tolist()

# ===== Layout ===== #
layout = dbc.Col([
                html.H1("Viabilidade Econômica", className="text-primary"),
                html.P("By Diogo Marin", className="text-info"),
                html.Hr(),

            # ---- PERFIL ---- #
                dbc.Button(id="botao_avatar",
                           children=[html.Img(src="/assets/img_business.png", id="avatar_change", alt="Avatar", className="perfil_avatar")],
                           style={'background-color': 'transparent', 'border-color': 'transparent'}),

            # ---- CADASTRO INVESTIMENTO ---- #
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
                                dbc.Label("Descrição:"),
                                dbc.Input(placeholder="Ex.: Aquisição de empresa concorrente", id= "txt_investimento"),
                            ], width=12),

                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.Label("Categoria:"),
                                dbc.Select(id="select_categoria", options=[{"label": i, "value": i} for i in categorias], value="")
                            ], width=4),

                            dbc.Col([
                                html.Label("Prioridade:"),
                                dbc.Select(id="select_prioridade", options=[{"label": i, "value": i} for i in prioridades], value="")
                            ], width=4, style={"margin-left": "20px"}),

                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.Label("Investimento Inicial ?"),
                                dbc.RadioItems(options=[{"label": "Sim", "value": 1},
                                                       {"label": "Não", "value": 2}],
                                                       value=[],
                                                       id="radioitems_investimento_inicial",
                                                       inline=True),
                            ], width=4),

                            dbc.Col([
                                html.Label("Capital Inicial Investido (R$):"),
                                dbc.Input(placeholder="10000", id="valor_investimento_inicial", value="")
                            ], width=4),

                            dbc.Col([
                                html.Label("Data do Investimento Inicial:"),
                                dcc.DatePickerSingle(id="data_inicial_investimento",
                                                     min_date_allowed=date(2020, 1, 1),
                                                     max_date_allowed=date(2030, 1, 1),
                                                     date=datetime.today(),
                                                     style={"with": "100%"}),
                            ], width=3, style={"margin-left": "20px"}),

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

            # ---- CADASTRO RECEITA / DESPESA / DEPRECIAÇÃO ---- #
            html.Div([
                dbc.Row([
                    dbc.Button("Receita", color="success", id="open_nova_receita"),
                ]),

                dbc.Row([
                    dbc.Button("Despesa", color="danger", id="open_nova_despesa"),
                ]),             

                dbc.Row([
                    dbc.Button("Depreciação", color="warning", id="open_nova_depreciacao"),
                ]),
                
                # --- MODAL RECEITA --- #                            
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Adicione uma receita futura")),
                    
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Descrição:"),
                                dbc.Input(placeholder="Ex.: Venda de 'n' unidades do produto 'x'", id= "txt_receita"),
                            ], width=7),

                            dbc.Col([
                                dbc.Label("Valor (R$):"),
                                dbc.Input(placeholder="1000", id= "valor_receita"),
                            ], width=3, style={"margin-left": "20px"}),                            

                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.Label("Classificação:"),
                                dbc.Select(id="select_classificao_receita", options=[{"label": i, "value": i} for i in classificacao_receita], value="")
                            ], width=4),

                            dbc.Col([
                                html.Label("Data Prevista:"),
                                dcc.DatePickerSingle(id="data_prevista_receita",
                                                     min_date_allowed=date(2020, 1, 1),
                                                     max_date_allowed=date(2030, 1, 1),
                                                     date=datetime.today(),
                                                     style={"with": "100%"}),
                            ], width=3, style={"margin-left": "20px"}),

                        ]),
                    ]),

                    dbc.ModalFooter([
                        dbc.Button("Adicionar Receita", id="salvar_receita", color="error"),
                        dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                    ]),                   
                
                ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal_nova_receita",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True),

                # --- MODAL DESPESA --- #                            
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Adicione uma despesa futura")),
                    
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Descrição:"),
                                dbc.Input(placeholder="Ex.: Compra de 'n' unidades do insumo 'w'", id= "txt_despesa"),
                            ], width=7),

                            dbc.Col([
                                dbc.Label("Valor (R$):"),
                                dbc.Input(placeholder="1000", id= "valor_despesa"),
                            ], width=3, style={"margin-left": "20px"}),                            

                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.Label("Classificação:"),
                                dbc.Select(id="select_classificao_despesa", options=[{"label": i, "value": i} for i in classificacao_despesa], value="")
                            ], width=4),

                            dbc.Col([
                                html.Label("Data Prevista:"),
                                dcc.DatePickerSingle(id="data_prevista_despesa",
                                                     min_date_allowed=date(2020, 1, 1),
                                                     max_date_allowed=date(2030, 1, 1),
                                                     date=datetime.today(),
                                                     style={"with": "100%"}),
                            ], width=3, style={"margin-left": "20px"}),

                        ]),
                    ]),

                    dbc.ModalFooter([
                        dbc.Button("Adicionar Despesa", id="salvar_despesa", color="error"),
                        dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_despesa", placement="left", trigger="click"),
                    ]),                   
                
                ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal_nova_despesa",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True),

                # --- MODAL DEPRECIAÇÃO --- #                            
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Adicione uma depreciação futura")),
                    
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Descrição:"),
                                dbc.Input(placeholder="Ex.: Computadores do escritório 'A' atingiram 1/4 da vida útil", id= "txt_depreciacao"),
                            ], width=7),

                            dbc.Col([
                                dbc.Label("Valor Inicial (R$):"),
                                dbc.Input(placeholder="1000", id= "valor_depreciacao_inicial"),
                            ], width=2, style={"margin-left": "20px"}),

                            dbc.Col([
                                dbc.Label("Valor Atual (R$):"),
                                dbc.Input(placeholder="750", id= "valor_depreciacao_atual"),
                            ], width=2, style={"margin-left": "20px"}),                           

                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.Label("Classificação:"),
                                dbc.Select(id="select_classificao_depreciacao", options=[{"label": i, "value": i} for i in classificacao_depreciacao], value="")
                            ], width=4),

                            dbc.Col([
                                html.Label("Data Prevista:"),
                                dcc.DatePickerSingle(id="data_prevista_depreciacao",
                                                     min_date_allowed=date(2020, 1, 1),
                                                     max_date_allowed=date(2030, 1, 1),
                                                     date=datetime.today(),
                                                     style={"with": "100%"}),
                            ], width=3, style={"margin-left": "20px"}),

                        ]),
                    ]),

                    dbc.ModalFooter([
                        dbc.Button("Adicionar Depreciação", id="salvar_depreciacao", color="error"),
                        dbc.Popover(dbc.PopoverBody("Depreciação Salva"), target="salvar_depreciacao", placement="left", trigger="click"),
                    ]),                   
                
                ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal_nova_depreciacao",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True),

            ]),

        ], id="sidebar_completa")

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
@app.callback(
    Output("modal_nova_receita", "is_open"),
    Input("open_nova_receita", "n_clicks"),
    State("modal_nova_receita", "is_open"),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open

# Pop-up despesas
@app.callback(
    Output("modal_nova_despesa", "is_open"),
    Input("open_nova_despesa", "n_clicks"),
    State("modal_nova_despesa", "is_open"),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open

# Pop-up depreciacoes
@app.callback(
    Output("modal_nova_depreciacao", "is_open"),
    Input("open_nova_depreciacao", "n_clicks"),
    State("modal_nova_depreciacao", "is_open"),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open
