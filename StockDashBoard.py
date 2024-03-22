import dash
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
import CoinData
import dash_table
import pandas as pd
from collections import OrderedDict

try:

    CoinData.wbs.start()

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div(id='parent', children=[
        html.H1(id='H1', children='Market Info', style={'textAlign': 'center',
                                                  'marginTop': 40, 'marginBottom': 40}),

        html.Div(

        dcc.Markdown('''
        ### Usefull Links
        - [Coinbase Pro](https://pro.coinbase.com/trade/BTC-USD)
        - [Open Sea](https://opensea.io/)
        - [Ether Scan](https://etherscan.io/)
            
        '''),
            style={'width': '30%', 'display': 'inline-block', 'outline': '1px solid Grey',
                   'padding': '10px',
                   'margin-right': '20px',
                   'margin-left': '20px',
                   'border-radius': '5px'}
        ),

        html.Div(

            dcc.Markdown('''
       ### Features 
       - *Directional Order Flow*
       - *Level 2 Order Book*
       - *5min Candle Chart*
       '''),
            style={'width': '30%', 'display': 'inline-block', 'outline': '1px solid Grey',
                   'padding': '10px',
                   'margin-right': '20px',
                   'border-radius': '5px'}
        ),

        html.Div(

                dcc.Markdown('''
           ### About 
           - Blank
           - Blank
           - Blank
           '''),
                style={'width': '30%', 'display': 'inline-block', 'outline': '1px solid Grey',
                       'padding': '10px',
                       'border-radius': '5px'}
            ),

        html.H3(
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
                                                         }),

            dcc.Interval(
                id='interval-component',
                interval=1*1000,
                n_intervals=0,
            ),

            html.Div(

                dash_table.DataTable(
                    id='order_book',
                    data=[],
                    columns=[],
                    style_cell={'textAlign': 'left',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                                'maxWidth': 0
                                },
                    style_as_list_view=True,
                    style_data_conditional=[
                        {
                            'if': {
                                'filter_query': '{Price} = 0',
                                'column_id': 'Price'
                            },
                            'backgroundColor': 'green',
                            'color': 'white'
                        },
                        {
                            'if': {
                                'filter_query': '{Price} = 0',
                                'column_id': 'Price'
                            },
                            'backgroundColor': 'red',
                            'color': 'white'
                        },

                    ],
                ),
                style={'margin-left': '85px',
                       'margin-top': '20px',
                       'margin-bottom': '20px',
                       'width': '30%'}
            )],
            style={'display': 'flex', 'outline': '1px solid Grey',
                   'margin-top': '25px',
                   'margin-left': '20px',
                   'margin-right': '20px',
                   'border-radius': '5px'}

        ),

        dcc.Interval(
            id='interval_orderbook',
            interval=1 * 300,
            n_intervals=0
        ),

        html.Div([

            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='View Positions', value='tab-1'),
                dcc.Tab(label='View Trades', value='tab-2'),
                dcc.Tab(label='Download Trades', value='tab-3'),
                dcc.Tab(label='View Account Stats', value='tab-4')
            ]),
            html.Div(id='tabs-content')

        ],
            style={
                'margin-top': '20px',
                'margin-left': '20px',
                'margin-right': '20px'
            }


        ),

        html.Div(
            id='active_product',
            key='BTC'
        )

    ])

    active_product = 'BTC-USD'

    @app.callback(Output(component_id='trades', component_property='figure'),#Output(component_id='active_product', component_proprty='key')
                  [Input(component_id='BTC', component_property='n_clicks'),
                   Input(component_id='ETH', component_property='n_clicks'),
                   Input(component_id='ADA', component_property='n_clicks'),
                   Input(component_id='SOL', component_property='n_clicks'),
                   Input(component_id='DOT', component_property='n_clicks'),
                   Input(component_id='RBN', component_property='n_clicks'),
                   Input(component_id='XTZ', component_property='n_clicks'),
                   Input(component_id='interval-component', component_property='n_intervals')])
                   #State(component_id='active_product', component_property='key'))
    def graph_update(a, b, c, d, e, f, g, nn):
        global active_product
        click_data = dash.callback_context.triggered
        #print(key)
        product = (str(click_data[0]['prop_id']).split('.'))[0]
        if product == 'interval-component':
            data = CoinData.obj.get_size_data(f'{active_product}')
            fig = px.line(data)
            fig.update_layout(title=f'Trade Pulls {active_product}',
                              xaxis_title='Transactions',
                              yaxis_title='Volume'

                              )
        else:
            if len(product) != 3:
                pass
            else:
                active_product = f'{product}-USD'
            data = CoinData.obj.get_size_data(f'{active_product}')
            fig = px.line(data)
            fig.update_layout(title=f'Trade Pulls {product}-USD',
                              xaxis_title='Transactions',
                              yaxis_title='Volume'
                              )
        return fig


    @app.callback([Output(component_id='order_book', component_property='data'),
                  Output(component_id='order_book', component_property='columns'),
                  Output(component_id='order_book', component_property='style_data_conditional')],
                  Input(component_id='interval_orderbook', component_property='n_intervals'))
    def order_book_update(n):
        global active_product
        data_frame, obid, oask = CoinData.obj.get_book_df(active_product)
        new_conds = [
            {
                'if': {
                    'filter_query': '{Price} = ' + f'{obid}',
                    'column_id': 'Price'
                },
                #'backgroundColor': 'MediumSeaGreen',
                'color': 'green',
                'font-weight': 'bold'


            },
            {
                'if': {
                    'filter_query': '{Price} = ' + f'{oask}',
                    'column_id': 'Price'
                },
                #'backgroundColor': 'LightCoral',
                'color': 'red',
                'font-weight': 'bold'
            }
        ]

        val_1 = data_frame.to_dict('records')
        val_2 = [{'id': c, 'name': c} for c in data_frame.columns]
        return val_1, val_2, new_conds


    @app.callback(Output('tabs-content', 'children'),
                  Input('tabs', 'value'))
    def render_content(tab):
        if tab == 'tab-1':
            return html.Div([
                html.H3('Open positions',
                        style={'outline': '2px solid CornFlowerBlue'})
            ])
        elif tab == 'tab-2':
            return html.Div([
                html.H3('Viewing Trade History',
                        style={'outline': '2px solid CornFlowerBlue'})
            ])
        elif tab == 'tab-3':
            return html.Div([
                html.H3('Download Trade Data',
                        style={'outline': '2px solid CornFlowerBlue'})
            ])
            pass
        elif tab == 'tab-4':
            return html.Div([
                html.H3('Account Data',
                        style={'outline': '2px solid CornFlowerBlue'})
            ])
            pass


    if __name__ == '__main__':
        app.run_server(debug=False)

finally:
    CoinData.wbs.close()
    pass
