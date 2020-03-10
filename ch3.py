#!/usr/bin/env python
import plotly.graph_objects as go
import pandas as pd

z_data = pd.read_csv('trial.csv')
z2_data = pd.read_csv('set2.csv')
fig = go.Figure(data=[
    go.Surface(
    x = [-6, -5,-4,-3,-2,-1,0,1,2,3,4,5,6], 
    y = [-6, -5,-4,-3,-2,-1,0,1,2,3,4,5,6],
    z=z2_data),
    go.Surface(
    x = [-6, -5,-4,-3,-2,-1,0,1,2,3,4,5,6], 
    y = [-6, -5,-4,-3,-2,-1,0,1,2,3,4,5,6],
    z=z_data.values)])

fig.update_layout(title='ch3_ci', autosize=False,
                  width=1500, height=1500,
                  margin=dict(l=65, r=50, b=65, t=90,
                  scene = dict(
                      xaxis = dict(title = 'h/GD [Angs]'),
                      yaxis = dict(title = 'g/NAC [Angs]')
                  )))

fig.show()
 