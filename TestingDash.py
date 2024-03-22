import dash
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px
import plotly.tools as pt
from dash.dependencies import Input, Output, State
import matplotlib.pyplot as plt
import CoinData
import dash_table
import pandas as pd
from collections import OrderedDict
import GraphData as gd

grapher_object = gd.FigureMaker()

try:

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div(id='parent', children=[
        html.H1(id='H1', children='Market Info', style={'textAlign': 'center',
                                                        'marginTop': 40, 'marginBottom': 40}),


        html.H2(
            'Products',
            style={'font-size': '30px',
                   'margin-top': '10x',
                   'color': 'black',
                   'text-align': 'center'}

        ),

        html.Div([

            html.Div(

                html.Button("BTC-USD", id="BTC", value='BTC', n_clicks=0),
                style={'padding': '5px', 'display': 'inline-block',
                       'margin-top': '20px',
                       'margin-left': '20px',
                       'margin-bottom': '20px'},

            ),

            html.Div(

                html.Button("ETH-USD", id="ETH", value='ETH', n_clicks=0),
                style={'padding': '5px', 'display': 'inline-block'},

            ),

            html.Div(

                html.Button("ADA-USD", id="ADA", value='ADA', n_clicks=0),
                style={'padding': '5px', 'display': 'inline-block'},

            ),

            html.Div(

                html.Button("XTZ-USD", id="XTZ", value='XTZ', n_clicks=0),
                style={'padding': '5px', 'display': 'inline-block'},

            ),

            html.Div(

                html.Button("SOL-USD", id="SOL", value="SOL", n_clicks=0),
                style={'padding': '5px', 'display': 'inline-block'},

            ),

            html.Div(

                html.Button("DOT-USD", id="DOT", value='DOT', n_clicks=0),
                style={'padding': '5px', 'display': 'inline-block'},

            ),

            html.Div(

                html.Button("RBN-USD", id="RBN", value='RBN', n_clicks=0),
                style={'padding': '5px', 'display': 'inline-block'},

            )
        ],
            style={'margin-left': '20px',
                   'margin-right': '20px',
                   'margin-top': '20px',
                   'outline': '1px solid Grey',
                   'border-radius': '5px'
                   }

        ),

        html.Div([
            dcc.Graph(id='trades', figure={}, style={'width': '60%',
                                                     'margin-left': '15x',
                                                     'margin-top': '20x'
                                                     },
                      )]
                )

        ])


    @app.callback([Output(component_id='trades', component_property='figure'), ],
                  [Input(component_id='BTC', component_property='n_clicks'),
                   Input(component_id='ETH', component_property='n_clicks'),
                   Input(component_id='ADA', component_property='n_clicks'),
                   Input(component_id='SOL', component_property='n_clicks'),
                   Input(component_id='DOT', component_property='n_clicks'),
                   Input(component_id='RBN', component_property='n_clicks'),
                   Input(component_id='XTZ', component_property='n_clicks'),
                   ])
    def graph_update(a, b, c, d, e, f, g):
        click_data = dash.callback_context.triggered
        product = (str(click_data[0]['prop_id']).split('.'))[0]
        print(product)

        f = grapher_object.get_graph('DOT-USD', 3600)

        fig = pt.mpl_to_plotly(f)

        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)

finally:
    pass

