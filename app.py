import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from collections import deque, Counter

########### Define your variables ######

myheading1='Why are you yelling?'
initial_value='I dont know'
longtext='''
        _Suggestions for you:_
        * Kayak
        * Mr. Owl ate my metal worm
        * Was it a car or a cat i saw?
        * Rats live on no evil star
        '''
tabtitle = 'Palindromes'
sourceurl = 'https://www.grammarly.com/blog/16-surprisingly-funny-palindromes/'
githublink = 'https://github.com/mgeisreiter/dash-simple-callback'

########### Define a function for your callback:
def my_function(letters):
    return(letters[::-1])

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div(children=[dcc.Markdown(longtext)]),
    dcc.Input(id='my-id', value=initial_value, type='text'),
    html.Div(id='my-div'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    palin=my_function(input_value)
    return f"You've entered '{input_value}', and your output is '{palin}'"
