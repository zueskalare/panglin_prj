print("this file is deprecated")
exit

import argparse as parse
import numpy as np
import plotly.graph_objects as go
import os

import permittivitycalc as pc
import src.plot_layout as plot_layout
import src.agent as agent
import scipy.signal as signal
import datetime
time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name = '/Volumes/tianjie 1/code/research/panglin_prj/data/test_2023_3_27/SL.s2p'

for _airline in ['VAL']:
    for _l in range(1,10):
            
        net,airline = agent.get_airline(file_name,L=_l,airline=_airline,density=2.1,net_f_unit='ghz')
        _dir = f'result/SL_{time}/{_airline}/{_l}'
        os.system('mkdir -p '+_dir)
        x_ = net.f/1e9
        fig = agent.draw_common(y=[net.s_db[:,0,0],net.s_db[:,0,1],net.s_db[:,1,0],net.s_db[:,1,1]],x=[x_,x_,x_,x_],name_list=['S11','S12','S21','S22'],x_title='Frequency(GHz)',y_title='S11(db)')
        fig.write_image(f'{_dir}/S.png')

        fig2 = agent.draw_common(y=[net.s_deg[:,0,0],net.s_deg[:,0,1],net.s_deg[:,1,0],net.s_deg[:,1,1]],x=[x_,x_,x_,x_],name_list=['S11','S12','S21','S22'],x_title='Frequency(GHz)',y_title='Phase(deg)',color=plot_layout.color['jianbian'][0])
        fig2.write_image(f'{_dir}/S_phase.png')


        ans = airline.avg_dielec
        ans = signal.savgol_filter(ans, 101, 3)
        fig3 = agent.draw_common(y=[ans],x=[x_],name_list=['Primitivity'],x_title='Frequency(GHz)',y_title='Permitivity',show_legend=False)
        fig3.write_image(f'{_dir}/pri.png')
        
        


        ans = airline.avg_mu_real
        ans = signal.savgol_filter(ans, 101, 3)
        fig4 = agent.draw_common(y=[ans],x=[x_],name_list=['Permitivity'],x_title='Frequency(GHz)',y_title='Permeability_Real',show_legend=False)
        fig4.write_image(f'{_dir}/per_real.png')


        ans = airline.avg_mu_imag
        ans = signal.savgol_filter(ans, 101, 3)
        fig5 = agent.draw_common(y=[ans],x=[x_],name_list=['Permitivity'],x_title='Frequency(GHz)',y_title='Permeability_Imag',show_legend=False)
        fig5.write_image(f'{_dir}/per_imag.png')


#denoise additive noise in time domain
# https://stackoverflow.com/questions/20618804/how-to-smooth-a-curve-in-the-right-way

# signal filtering scipy.signal

#explain the flow of permittivity calculation3
# 1. read the s2p file
# 2. calculate the s-parameters
# 3. calculate the permittivity and permeability
# 4. calculate the average permittivity and permeability
# 5. plot the s-parameters
# 6. plot the permittivity and permeability
# 7. plot the average permittivity and permeability


