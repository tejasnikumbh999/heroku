import dash
import dash_auth
from dash.dependencies import Input, Output, State
from dash import dcc, html
 
USERNAME_PASSWORD_PAIRS = [
    ['nethu', '12345'],['guvi', 'guvi']
]
 
app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server

app.layout = html.Div([
   html.Div('Convert Temperature'),
   'Celsius',
   dcc.Input(
       id="celsius",
       value=0.0,
       type="number"
   ),
   ' = Fahrenheit',
   dcc.Input(
       id="fahrenheit",
       value=32.0,
       type="number",
   ),
])
 
@app.callback(
   Output("celsius", "value"),
   Output("fahrenheit", "value"),
   Input("celsius", "value"),
   Input("fahrenheit", "value"),
)
def sync_input(celsius, fahrenheit):
   ctx = dash.callback_context
   input_id = ctx.triggered[0]["prop_id"].split(".")[0]
   if input_id == "celsius":
       fahrenheit= None if celsius is None else (float(celsius) * 9/5) + 32
   else:
       celsius = None if fahrenheit is None else (float(fahrenheit) - 32) * 5/9
   return celsius, fahrenheit
 
if __name__ == "__main__":
   app.run_server(debug=True)
