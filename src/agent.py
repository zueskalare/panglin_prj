# import argparse as parse
import numpy as np
import plotly.graph_objects as go
import permittivitycalc as pc
from . import pre
import os 
import skrf as rf
from os.path import split
import plotly.graph_objects as go
from . import plot_layout 


def get_airline(data_array, in_file,L=2,airline='VAL',density=2.1):
    s = pc.AirlineData(L,airline,dataArray=data_array,file=in_file,name=split(in_file)[1],date=None,nrw=True,\
        bulk_density=density,temperature=None,corr=False,solid_dielec=None,solid_losstan=None,particle_diameter=None,\
        particle_density=None,normalize_density=False,norm_eqn='LI',shorted=False,freq_cutoff=100000000.0)
    
    return s


def draw_common(x:list,y:list,name_list:list,x_title,y_title,color = plot_layout.color['jianbian'][2],show_legend=True):
    '''
    length no more than 5
    x 为数组的数组
    '''
    trace = []
    shape = ['square-open','star-open','circle-open','triangle-up-open','diamond-open']
    
    layout = plot_layout.layout
    layout['showlegend']=show_legend
    layout['xaxis']['title']['text'] = f'<b>{x_title}</b>'
    layout['yaxis']['title']['text'] = f'<b>{y_title}</b>'
    
    for id,(_x, _y,_name) in enumerate(zip(x,y,name_list)):
        trace.append(go.Scatter(
            
                x = _x,
                y = _y,
                name = f'<b>{_name}</b>',
                mode='lines+markers',
                marker = dict(
                    size = 10,
                    color = color[id],
                    symbol = shape[id],
                    line=dict(
                        width= 4
                    )
                ),
                line = dict(
                    width = 4,
                    color = color[id]
                )

            )
        )
        
    fig = go.Figure(data=trace,layout=layout)
    return (fig)
    
    
    