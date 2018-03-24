
import plotly
plotly.tools.set_credentials_file(username='iremoze', api_key='N0pN2Vqt1NphEV7q8jLC')

import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5],
    y=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
)
trace2 = go.Bar(
    x=[0, 1, 2, 3, 4, 5],
    y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
)

data = [trace1, trace2]
py.plot(data, filename='bar-line')