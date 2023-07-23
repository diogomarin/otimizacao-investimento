import dash
import dash_bootstrap_components as dbc

estilos = []
dbc_css = 

app = dash.Dash(__name__, external_stylesheets==estilos + [dbc_css])

app.config['suppress_callback_expections'] = True
app.scripts.config.serve_locally = True
server = app.server