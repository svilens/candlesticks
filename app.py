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
    app.run_server(debug=False, use_reloader=False)