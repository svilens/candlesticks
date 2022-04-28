import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objs as go
import plotly.io as pio
pio.templates.default = "plotly_dark"
import time

def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    """ returns a (x, y) tuple or None if there is no intersection """
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)
 
    return x, y


def draw_candlestick(ticker, period='8d', interval='1h'):
    data = yf.download(tickers=ticker, period=period, interval=interval, threads=False)
    
    # convert time zone
    # try:
    #     data.index = data.index.tz_localize('America/New_York').tz_convert('Europe/Sofia')
    # except:
    #     data.index = data.index.tz_convert('Europe/Sofia')
    
    data['MA5'] = data['Close'].rolling(5).mean()
    data['MA20'] = data['Close'].rolling(20).mean()
    
    df = data[['MA5', 'MA20']].reset_index().rename(columns={'index':'time', 'Datetime':'time', 'Date':'time'})
    
    # identify the times when short-term moving avg intersects the long-term one
    x_positions = [x for x in range(len(df))]
    breakevens = []
    
    for x_pos in x_positions:
        if pd.isna(df.iloc[x_pos, -1]):
            continue
        elif pd.isna(df.iloc[x_pos - 1, -1]):
            continue
        else:
            ax1 = bx1 = x_pos-1
            ax2 = bx2 = x_pos
            ay1 = df.iloc[x_pos-1, -2]
            ay2 = df.iloc[x_pos, -2]
            by1 = df.iloc[x_pos-1, -1]
            by2 = df.iloc[x_pos, -1]
            
            intersect = line_intersect(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
            
            if intersect != None:
                breakevens.append(df['time'][x_pos-1])
    
    # for each breakeven point define whether it's a buy or sell advice
    labels = []
    
    for breakeven in breakevens:
        i = df.loc[df['time'] == breakeven].index[0]
        prev_ma5 = df.loc[df.index == i-1, 'MA5'].values[0]
        prev_ma20 = df.loc[df.index == i-1, 'MA20'].values[0]
        if prev_ma5 > prev_ma20:
            labels.append('SELL')
        else:
            labels.append('BUY')
    
    
    # draw candlestick
    """
    Source: https://levelup.gitconnected.com/how-i-tripled-my-return-on-bitcoin-using-mathematics-algorithms-and-python-347edd9b5625
    """
    fig = go.Figure()
    fig.add_trace(
        go.Candlestick(
            x = data.index,
            open = data['Open'],
            high = data['High'],
            low = data['Low'],
            close = data['Close'],
            name = ticker))
    
    # add moving average
    fig.add_trace(go.Scatter(x=data.index, y=data['MA20'],
                             line=dict(color='purple', width=1.5),
                             name='Long-term MA'))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA5'],
                             line=dict(color='orange', width=1.5),
                             name='Short-term MA'))
    
    # add buttons
    fig.update_xaxes(
        rangeslider_visible = True,
        rangeselector = dict(
            buttons = list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=1, label="1h", step="hour", stepmode="backward"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(count=1, label="1d", step="day", stepmode="backward"),
                dict(count=3, label="3d", step="day", stepmode="backward"),
                dict(count=5, label="5d", step="day", stepmode="backward"),
                dict(count=7, label="WTD", step="day", stepmode="todate"),
                dict(step="all")
            ]),
            bgcolor='rgba(50,50,50,0)',
            activecolor='rgba(100,100,100,0)'
            
        )
    )
    fig.update_layout(title=f'Ticker: {ticker}', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    
    # add breakeven points with the respective coloring
    for i, breakeven in list(enumerate(breakevens)):
        if labels[i] == 'SELL':
            label_color = 'coral'
        else:
            label_color = 'cyan'
        fig.add_trace(go.Scatter(
            x=df.loc[df['time'] == breakeven, 'time'],
            y=df.loc[df['time'] == breakeven, 'MA20'],
            mode='markers',
            marker=dict(
                color=label_color, size=9,
                line=dict(width=1, color='DarkSlateGrey')),
            name=labels[i], showlegend=False))
    
    return fig