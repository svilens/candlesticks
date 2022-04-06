import plotly.graph_objs as go
from plotly.offline import plot
import time
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from functions import line_intersect, draw_candlestick


app = dash.Dash(
    name='Candlesticks',
    #external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_stylesheets=['./assets/bootstrap_adjusted.css'],
)
app.title = 'Candlesticks'

options_interval = [
    {'label':'1 minute', 'value':'1m'},
    {'label':'2 minutes', 'value':'2m'},
    {'label':'5 minutes', 'value':'5m'},
    {'label':'15 minutes', 'value':'15m'},
    {'label':'30 minutes', 'value':'30m'},
    {'label':'1 hour', 'value':'1h'},
    {'label':'1.5 hours', 'value':'90m'},
    {'label':'1 day', 'value':'1d'},
    {'label':'5 days', 'value':'5d'},
    {'label':'1 week', 'value':'1wk'},
    {'label':'1 month', 'value':'1mo'},
    {'label':'3 months', 'value':'3mo'}]


tabs = html.Div([
    dcc.Tabs(
        id = 'tabs-css',
        parent_className = 'custom-tabs',
        className = 'custom-tabs-container',
        children = [
            dcc.Tab(
                label = "Crypto",
                className = "custom-tab",
                selected_className = "custom-tab--selected",
                children = [
                    html.Br(),
                    html.Br(),
                    html.H4('Bitcoin'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_btc',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_btc',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_btc', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_btc"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Bitcoin Cash'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_bch',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_bch',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_bch', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_bch"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Ethereum Classic'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_etc',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_etc',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_etc', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_etc"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Ether'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_eth',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_eth',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_eth', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_eth"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Litecoin'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_ltc',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_ltc',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_ltc', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_ltc"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Ripple'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_xrp',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_xrp',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_xrp', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_xrp"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Stellar'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_xlm',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_xlm',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_xlm', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_xlm"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Dash'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_dash',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_dash',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_dash', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_dash"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('EOS'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_eos',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_eos',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_eos', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_eos"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Zcash'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_zec',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_zec',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_zec', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_zec"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('0x'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_zrx',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_zrx',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_zrx', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_zrx"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Aave'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_aave',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_aave',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_aave', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_aave"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Algorand'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_algo',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_algo',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_algo', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_algo"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Ankr'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_ankr',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_ankr',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_ankr', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_ankr"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Bancor'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_bnt',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_bnt',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_bnt', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_bnt"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Band Protocol'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_band',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_band',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_band', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_band"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Basic Attention Token'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_bat',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_bat',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_bat', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_bat"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Cardano'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_ada',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_ada',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_ada', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_ada"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Celo'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_celo',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_celo',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_celo', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_celo"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Chainlink'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_link',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_link',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_link', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_link"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Compound'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_comp',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_comp',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_comp', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_comp"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Curve Finance'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_crv',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_crv',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_crv', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_crv"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('Decentraland'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_mana',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_mana',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_mana', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_mana"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.H4('DogeCoin'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_doge',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_doge',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_doge', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_doge"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    # html.H4('Enjin'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_enj',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_enj',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_enj', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_enj"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('Filecoin'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_fil',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_fil',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_fil', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_fil"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('iExec'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_rlc',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_rlc',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_rlc', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_rlc"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('Kyber'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_knc',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_knc',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_knc', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_knc"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('Loopring'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_lrc',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_lrc',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_lrc', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_lrc"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('Matic/Polygon'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_matic',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_matic',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_matic', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_matic"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('Mirror Protocol'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_mir',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_mir',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_mir', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_mir"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('NKN (New Kind of Network)'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_nkn',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_nkn',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_nkn', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_nkn"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('NuCypher'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_nu',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_nu',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_nu', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_nu"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('OMG Network'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_omg',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_omg',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_omg', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_omg"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('Orchid'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_oxt',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_oxt',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_oxt', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_oxt"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('Storj'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_storj',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_storj',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_storj', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_storj"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('SushiSwap'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_sushi',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_sushi',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_sushi', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_sushi"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('Synthetix'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_snx',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_snx',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_snx', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_snx"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    html.H4('Tezos'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_xtz',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_xtz',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_xtz', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_xtz"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    # html.H4('UMA'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_uma',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_uma',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_uma', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_uma"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                    # html.H4('yearn.finance'),
                    # html.Br(),
                    # html.Div([
                    #     html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(
                    #             id='interval_yfi',
                    #             className='dropdown',
                    #             options=options_interval,
                    #             placeholder='Select time interval',
                    #             value='1d',
                    #             style=dict(width='50%')
                    #         ),
                    #         dcc.Input(
                    #             id='period_yfi',
                    #             className='dropdown',
                    #             type='number',
                    #             placeholder='Select period (days)',
                    #             style=dict(width='20%'),
                    #             value=100, min=1, max=100000, step=1,
                    #             debounce=True # press Enter to send the input
                    #         )
                    #     ]),
                    #     html.Div([
                    #         dcc.Loading(
                    #             id='output_loader_yfi', type='default',
                    #             children=[
                    #                 html.Div(dcc.Graph(id="output_yfi"))
                    #             ]
                    #         )
                    #     ]),
                    #     html.Br()
                    # ]),
                ]
            ),
            dcc.Tab(
                label = "Forex",
                className = "custom-tab",
                selected_className = "custom-tab--selected",
                children = [
                    html.Br(),
                    html.Br(),
                    html.H4('USD/JPY'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_usdjpy',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_usdjpy',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_usdjpy', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_usdjpy"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('USD/AUD'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_usdaud',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_usdaud',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_usdaud', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_usdaud"))
                                ]
                            )
                        ]),
                        html.Br(),
                    ]),
                    html.Br(),
                    html.H4('USD/GBP'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_usdgbp',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_usdgbp',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_usdgbp', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_usdgbp"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('USD/EUR'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_usdeur',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_usdeur',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_usdeur', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_usdeur"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('USD/CHF'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_usdchf',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_usdchf',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_usdchf', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_usdchf"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('USD/RUB'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_usdrub',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_usdrub',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_usdrub', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_usdrub"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('EUR/GBP'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_eurgbp',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_eurgbp',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_eurgbp', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_eurgbp"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('EUR/JPY'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_eurjpy',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_eurjpy',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_eurjpy', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_eurjpy"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                ]
            ),
            dcc.Tab(
                label = "Stocks",
                className = "custom-tab",
                selected_className = "custom-tab--selected",
                children = [
                    html.Br(),
                    html.Br(),
                    html.H4('Apple'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_aapl',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_aapl',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_aapl', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_aapl"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Microsoft'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_msft',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_msft',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_msft', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_msft"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Tesla'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_tsla',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_tsla',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_tsla', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_tsla"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Experian'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_expn',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_expn',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_expn', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_expn"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Devon Energy Corp'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_dvn',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_dvn',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_dvn', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_dvn"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Antero Resources'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_ar',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_ar',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_ar', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_ar"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Alcoa'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_aa',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_aa',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_aa', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_aa"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Freeport-McMoRan'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_fcx',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_fcx',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_fcx', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_fcx"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('ExxonMobil'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_xom',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_xom',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_xom', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_xom"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Glencore'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_glncy',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_glncy',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_glncy', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_glncy"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Antero Midstream Corp'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_am',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_am',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_am', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_am"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Agnico Eagle Mines'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_aem',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_aem',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_aem', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_aem"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Apache'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_apa',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_apa',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_apa', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_apa"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    html.Br(),
                    html.H4('Arconic'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_arnc',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_arnc',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_arnc', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_arnc"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                    

                ]
            ),
            dcc.Tab(
                label = "Futures",
                className = "custom-tab",
                selected_className = "custom-tab--selected",
                children = [
                    html.Br(),
                    html.Br(),
                    html.H4('Gold'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_gc',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_gc',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_gc', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_gc"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                ]
            ),
            dcc.Tab(
                label = "Indexes",
                className = "custom-tab",
                selected_className = "custom-tab--selected",
                children = [
                    html.Br(),
                    html.Br(),
                    html.H4('S&P 500'),
                    html.Br(),
                    html.Div([
                        html.P('Select time interval from the dropdown below and specify the length of the historical period in days.'),
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(
                                id='interval_sp500',
                                className='dropdown',
                                options=options_interval,
                                placeholder='Select time interval',
                                value='1d',
                                style=dict(width='50%')
                            ),
                            dcc.Input(
                                id='period_sp500',
                                className='dropdown',
                                type='number',
                                placeholder='Select period (days)',
                                style=dict(width='20%'),
                                value=100, min=1, max=100000, step=1,
                                debounce=True # press Enter to send the input
                            )
                        ]),
                        html.Div([
                            dcc.Loading(
                                id='output_loader_sp500', type='default',
                                children=[
                                    html.Div(dcc.Graph(id="output_sp500"))
                                ]
                            )
                        ]),
                        html.Br()
                    ]),
                ]
            )
        ]
    )
])

footer = html.Div(
    [
        html.Small("Data source: Yahoo Finance API"),
        html.Br(),
        html.Small("Designed by "),
        html.Small(html.A("Svilen Stefanov", href="https://www.linkedin.com/in/svilen-stefanov/", target="_blank")),
        html.Br(),
        html.Small(html.A("Source code", href="https://github.com/svilens/candlesticks/", target="_blank")),
    ], style={'font-style':'italic', 'padding-left':'10px', 'textAlign':'center'}
)

app.layout = html.Div([
    html.H1(children='Financial markets - Candlesticks', style={'padding-left':'5px'}),
    html.Br(),
    html.H6('A web app that downloads the latest financial markets data, draws a candlestick graph for each ticker and puts breakeven points for potentially good moments for short/long positions. All timezones are converted to GMT+3.'),
    html.Br(),
    tabs,
    footer
])


# callbacks
@app.callback(
        dash.dependencies.Output('output_btc', 'figure'),
    [
        dash.dependencies.Input('interval_btc', 'value'),
        dash.dependencies.Input('period_btc', 'value')
    ])
def update_btc(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='BTC-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_bch', 'figure'),
    [
        dash.dependencies.Input('interval_bch', 'value'),
        dash.dependencies.Input('period_bch', 'value')
    ])
def update_bch(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='BCH-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_etc', 'figure'),
    [
        dash.dependencies.Input('interval_etc', 'value'),
        dash.dependencies.Input('period_etc', 'value')
    ])
def update_etc(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='ETC-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_eth', 'figure'),
    [
        dash.dependencies.Input('interval_eth', 'value'),
        dash.dependencies.Input('period_eth', 'value')
    ])
def update_eth(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='ETH-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_ltc', 'figure'),
    [
        dash.dependencies.Input('interval_ltc', 'value'),
        dash.dependencies.Input('period_ltc', 'value')
    ])
def update_ltc(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='LTC-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_xrp', 'figure'),
    [
        dash.dependencies.Input('interval_xrp', 'value'),
        dash.dependencies.Input('period_xrp', 'value')
    ])
def update_xrp(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='XRP-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_xlm', 'figure'),
    [
        dash.dependencies.Input('interval_xlm', 'value'),
        dash.dependencies.Input('period_xlm', 'value')
    ])
def update_xlm(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='XLM-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_dash', 'figure'),
    [
        dash.dependencies.Input('interval_dash', 'value'),
        dash.dependencies.Input('period_dash', 'value')
    ])
def update_dash(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='DASH-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_eos', 'figure'),
    [
        dash.dependencies.Input('interval_eos', 'value'),
        dash.dependencies.Input('period_eos', 'value')
    ])
def update_eos(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='EOS-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_zec', 'figure'),
    [
        dash.dependencies.Input('interval_zec', 'value'),
        dash.dependencies.Input('period_zec', 'value')
    ])
def update_zec(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='ZEC-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_zrx', 'figure'),
    [
        dash.dependencies.Input('interval_zrx', 'value'),
        dash.dependencies.Input('period_zrx', 'value')
    ])
def update_zrx(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='ZRX-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_aave', 'figure'),
    [
        dash.dependencies.Input('interval_aave', 'value'),
        dash.dependencies.Input('period_aave', 'value')
    ])
def update_aave(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='AAVE-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_algo', 'figure'),
    [
        dash.dependencies.Input('interval_algo', 'value'),
        dash.dependencies.Input('period_algo', 'value')
    ])
def update_algo(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='ALGO-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_ankr', 'figure'),
    [
        dash.dependencies.Input('interval_ankr', 'value'),
        dash.dependencies.Input('period_ankr', 'value')
    ])
def update_ankr(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='ANKR-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_bnt', 'figure'),
    [
        dash.dependencies.Input('interval_bnt', 'value'),
        dash.dependencies.Input('period_bnt', 'value')
    ])
def update_bnt(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='BNT-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_band', 'figure'),
    [
        dash.dependencies.Input('interval_band', 'value'),
        dash.dependencies.Input('period_band', 'value')
    ])
def update_band(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='BAND-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_bat', 'figure'),
    [
        dash.dependencies.Input('interval_bat', 'value'),
        dash.dependencies.Input('period_bat', 'value')
    ])
def update_bat(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='BAT-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_ada', 'figure'),
    [
        dash.dependencies.Input('interval_ada', 'value'),
        dash.dependencies.Input('period_ada', 'value')
    ])
def update_ada(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='ADA-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_celo', 'figure'),
    [
        dash.dependencies.Input('interval_celo', 'value'),
        dash.dependencies.Input('period_celo', 'value')
    ])
def update_celo(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='CELO-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_link', 'figure'),
    [
        dash.dependencies.Input('interval_link', 'value'),
        dash.dependencies.Input('period_link', 'value')
    ])
def update_link(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='LINK-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_comp', 'figure'),
    [
        dash.dependencies.Input('interval_comp', 'value'),
        dash.dependencies.Input('period_comp', 'value')
    ])
def update_comp(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='COMP-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_crv', 'figure'),
    [
        dash.dependencies.Input('interval_crv', 'value'),
        dash.dependencies.Input('period_crv', 'value')
    ])
def update_crv(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='CRV-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_mana', 'figure'),
    [
        dash.dependencies.Input('interval_mana', 'value'),
        dash.dependencies.Input('period_mana', 'value')
    ])
def update_mana(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='MANA-USD', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_doge', 'figure'),
    [
        dash.dependencies.Input('interval_doge', 'value'),
        dash.dependencies.Input('period_doge', 'value')
    ])
def update_doge(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='DOGE-USD', period=period, interval=interval)
    return fig

# @app.callback(
#         dash.dependencies.Output('output_enj', 'figure'),
#     [
#         dash.dependencies.Input('interval_enj', 'value'),
#         dash.dependencies.Input('period_enj', 'value')
#     ])
# def update_enj(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='ENJ-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_fil', 'figure'),
#     [
#         dash.dependencies.Input('interval_fil', 'value'),
#         dash.dependencies.Input('period_fil', 'value')
#     ])
# def update_fil(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='FIL-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_rlc', 'figure'),
#     [
#         dash.dependencies.Input('interval_rlc', 'value'),
#         dash.dependencies.Input('period_rlc', 'value')
#     ])
# def update_rlc(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='RLC-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_knc', 'figure'),
#     [
#         dash.dependencies.Input('interval_knc', 'value'),
#         dash.dependencies.Input('period_knc', 'value')
#     ])
# def update_knc(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='KNC-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_lrc', 'figure'),
#     [
#         dash.dependencies.Input('interval_lrc', 'value'),
#         dash.dependencies.Input('period_lrc', 'value')
#     ])
# def update_lrc(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='LRC-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_matic', 'figure'),
#     [
#         dash.dependencies.Input('interval_matic', 'value'),
#         dash.dependencies.Input('period_matic', 'value')
#     ])
# def update_matic(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='MATIC-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_mir', 'figure'),
#     [
#         dash.dependencies.Input('interval_mir', 'value'),
#         dash.dependencies.Input('period_mir', 'value')
#     ])
# def update_mir(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='MIR-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_nkn', 'figure'),
#     [
#         dash.dependencies.Input('interval_nkn', 'value'),
#         dash.dependencies.Input('period_nkn', 'value')
#     ])
# def update_nkn(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='NKN-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_nu', 'figure'),
#     [
#         dash.dependencies.Input('interval_nu', 'value'),
#         dash.dependencies.Input('period_nu', 'value')
#     ])
# def update_nu(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='NU-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_omg', 'figure'),
#     [
#         dash.dependencies.Input('interval_omg', 'value'),
#         dash.dependencies.Input('period_omg', 'value')
#     ])
# def update_omg(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='OMG-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_oxt', 'figure'),
#     [
#         dash.dependencies.Input('interval_oxt', 'value'),
#         dash.dependencies.Input('period_oxt', 'value')
#     ])
# def update_oxt(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='OXT-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_storj', 'figure'),
#     [
#         dash.dependencies.Input('interval_storj', 'value'),
#         dash.dependencies.Input('period_storj', 'value')
#     ])
# def update_storj(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='STORJ-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_sushi', 'figure'),
#     [
#         dash.dependencies.Input('interval_sushi', 'value'),
#         dash.dependencies.Input('period_sushi', 'value')
#     ])
# def update_sushi(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='SUSHI-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_snx', 'figure'),
#     [
#         dash.dependencies.Input('interval_snx', 'value'),
#         dash.dependencies.Input('period_snx', 'value')
#     ])
# def update_snx(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='SNX-USD', period=period, interval=interval)
#     return fig

@app.callback(
        dash.dependencies.Output('output_xtz', 'figure'),
    [
        dash.dependencies.Input('interval_xtz', 'value'),
        dash.dependencies.Input('period_xtz', 'value')
    ])
def update_xtz(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='XTZ-USD', period=period, interval=interval)
    return fig

# @app.callback(
#         dash.dependencies.Output('output_uma', 'figure'),
#     [
#         dash.dependencies.Input('interval_uma', 'value'),
#         dash.dependencies.Input('period_uma', 'value')
#     ])
# def update_uma(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='UMA-USD', period=period, interval=interval)
#     return fig

# @app.callback(
#         dash.dependencies.Output('output_yfi', 'figure'),
#     [
#         dash.dependencies.Input('interval_yfi', 'value'),
#         dash.dependencies.Input('period_yfi', 'value')
#     ])
# def update_yfi(interval, period):
#     period = f'{str(period)}d'
#     fig = draw_candlestick(ticker='YFI-USD', period=period, interval=interval)
#     return fig

@app.callback(
        dash.dependencies.Output('output_usdjpy', 'figure'),
    [
        dash.dependencies.Input('interval_usdjpy', 'value'),
        dash.dependencies.Input('period_usdjpy', 'value')
    ])
def update_usdjpy(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='USDJPY=X', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_usdeur', 'figure'),
    [
        dash.dependencies.Input('interval_usdeur', 'value'),
        dash.dependencies.Input('period_usdeur', 'value')
    ])
def update_usdeur(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='USDEUR=X', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_usdgbp', 'figure'),
    [
        dash.dependencies.Input('interval_usdgbp', 'value'),
        dash.dependencies.Input('period_usdgbp', 'value')
    ])
def update_usdgbp(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='USDGBP=X', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_usdaud', 'figure'),
    [
        dash.dependencies.Input('interval_usdaud', 'value'),
        dash.dependencies.Input('period_usdaud', 'value')
    ])
def update_usdaud(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='USDAUD=X', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_usdchf', 'figure'),
    [
        dash.dependencies.Input('interval_usdchf', 'value'),
        dash.dependencies.Input('period_usdchf', 'value')
    ])
def update_usdchf(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='USDCHF=X', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_usdrub', 'figure'),
    [
        dash.dependencies.Input('interval_usdrub', 'value'),
        dash.dependencies.Input('period_usdrub', 'value')
    ])
def update_usdrub(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='USDRUB=X', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_eurgbp', 'figure'),
    [
        dash.dependencies.Input('interval_eurgbp', 'value'),
        dash.dependencies.Input('period_eurgbp', 'value')
    ])
def update_eurgbp(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='EURGBP=X', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_eurjpy', 'figure'),
    [
        dash.dependencies.Input('interval_eurjpy', 'value'),
        dash.dependencies.Input('period_eurjpy', 'value')
    ])
def update_eurjpy(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='EURJPY=X', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_aapl', 'figure'),
    [
        dash.dependencies.Input('interval_aapl', 'value'),
        dash.dependencies.Input('period_aapl', 'value')
    ])
def update_aapl(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='AAPL', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_msft', 'figure'),
    [
        dash.dependencies.Input('interval_msft', 'value'),
        dash.dependencies.Input('period_msft', 'value')
    ])
def update_msft(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='MSFT', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_tsla', 'figure'),
    [
        dash.dependencies.Input('interval_tsla', 'value'),
        dash.dependencies.Input('period_tsla', 'value')
    ])
def update_tsla(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='TSLA', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_expn', 'figure'),
    [
        dash.dependencies.Input('interval_expn', 'value'),
        dash.dependencies.Input('period_expn', 'value')
    ])
def update_expn(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='EXPN.L', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_dvn', 'figure'),
    [
        dash.dependencies.Input('interval_dvn', 'value'),
        dash.dependencies.Input('period_dvn', 'value')
    ])
def update_dvn(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='DVN', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_ar', 'figure'),
    [
        dash.dependencies.Input('interval_ar', 'value'),
        dash.dependencies.Input('period_ar', 'value')
    ])
def update_ar(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='AR', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_aa', 'figure'),
    [
        dash.dependencies.Input('interval_aa', 'value'),
        dash.dependencies.Input('period_aa', 'value')
    ])
def update_aa(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='AA', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_fcx', 'figure'),
    [
        dash.dependencies.Input('interval_fcx', 'value'),
        dash.dependencies.Input('period_fcx', 'value')
    ])
def update_fcx(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='FCX', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_xom', 'figure'),
    [
        dash.dependencies.Input('interval_xom', 'value'),
        dash.dependencies.Input('period_xom', 'value')
    ])
def update_xom(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='XOM', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_glncy', 'figure'),
    [
        dash.dependencies.Input('interval_glncy', 'value'),
        dash.dependencies.Input('period_glncy', 'value')
    ])
def update_glncy(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='GLNCY', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_am', 'figure'),
    [
        dash.dependencies.Input('interval_am', 'value'),
        dash.dependencies.Input('period_am', 'value')
    ])
def update_am(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='AM', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_aem', 'figure'),
    [
        dash.dependencies.Input('interval_aem', 'value'),
        dash.dependencies.Input('period_aem', 'value')
    ])
def update_aem(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='AEM', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_apa', 'figure'),
    [
        dash.dependencies.Input('interval_apa', 'value'),
        dash.dependencies.Input('period_apa', 'value')
    ])
def update_apa(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='APA', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_arnc', 'figure'),
    [
        dash.dependencies.Input('interval_arnc', 'value'),
        dash.dependencies.Input('period_arnc', 'value')
    ])
def update_arnc(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='ARNC', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_gc', 'figure'),
    [
        dash.dependencies.Input('interval_gc', 'value'),
        dash.dependencies.Input('period_gc', 'value')
    ])
def update_gc(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='GC=F', period=period, interval=interval)
    return fig

@app.callback(
        dash.dependencies.Output('output_sp500', 'figure'),
    [
        dash.dependencies.Input('interval_sp500', 'value'),
        dash.dependencies.Input('period_sp500', 'value')
    ])
def update_sp500(interval, period):
    period = f'{str(period)}d'
    fig = draw_candlestick(ticker='^GSPC', period=period, interval=interval)
    return fig

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)