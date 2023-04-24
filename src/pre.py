## This file is used to pre-process the data

import pandas as pd 
import numpy as np
import skrf as rf 



def pre2pc(in_file,out_file):
    '''
    if need 讲数据格式为real imag 转换为mag deg 输出
    '''
    network = rf.Network(in_file,f_unit='hz')

    s_mag = network.s_mag
    s_deg = network.s_deg
    
    freq = network.f
    f = open(out_file,'w')
    f.write('#\tS11_mag\tS11_deg\tS21_mag\tS21_deg\tS12_mag\tS12_deg\tS22_mag\tS22_deg\n')
    for i in range(len(freq)):
        f.write(f'{freq[i]}\t{s_mag[i][0,0]}\t{s_deg[i][0,0]}\t{s_mag[i][1,0]}\t{s_deg[i][1,0]}\t{s_mag[i][0,1]}\t{s_deg[i][0,1]}\t{s_mag[i][1,1]}\t{s_deg[i][1,1]}\n')
        
        
    f.close()
    

def save_network(network,out_file):
    '''
    save Network to file as format mag deg
    '''
    s_mag = network.s_mag
    s_deg = network.s_deg
    
    freq = network.f
    f = open(out_file,'w')
    f.write('#\tS11_mag\tS11_deg\tS21_mag\tS21_deg\tS12_mag\tS12_deg\tS22_mag\tS22_deg\n')
    for i in range(len(freq)):
        f.write(f'{freq[i]}\t{s_mag[i][0,0]}\t{s_deg[i][0,0]}\t{s_mag[i][1,0]}\t{s_deg[i][1,0]}\t{s_mag[i][0,1]}\t{s_deg[i][0,1]}\t{s_mag[i][1,1]}\t{s_deg[i][1,1]}\n')
        
        
    f.close()
    
    
def parser_file(in_file):
    '''
    应对 permitivitycal 需要 读取文件 输出 dataarray  格式为 hz S11_mag S11_deg S21_mag S21_deg S12_mag S12_deg S22_mag S22_deg
    '''
    network = rf.Network(in_file,f_unit='hz')
    freq = network.f
    s_mag = network.s_mag
    s_deg = network.s_deg
    res = np.array([[freq[i],s_mag[i][0,0],s_deg[i][0,0],s_mag[i][1,0],s_deg[i][1,0],s_mag[i][0,1],s_deg[i][0,1],s_mag[i][1,1],s_deg[i][1,1]] for i in range(len(freq))])
    return res

def parser_csv(in_csv):
    r'''
    当文件问csv格式时，读取文件
    输入必须为 hz mag deg 格式
    '''
    f= open(in_csv,'r')
    table = []
    for id, line in enumerate(f):
        if id == 2:
            head = line.strip().split(' ')
        if id < 3:
            continue
        else:
            table.append(line.strip().split(' '))
    f.close()
    res = np.array([[float(row[j]) if head[j].find('db')==-1 else rf.db_2_mag(float(row[j])) for j in range(len(row))] for row in table],dtype=np.float32)
    return res
    
    
def parser_network(network):
    '''
    The unit of frequency of network must be hz
    '''

    freq = network.f
    s_mag = network.s_mag
    s_deg = network.s_deg
    res = np.array([[freq[i],s_mag[i][0,0],s_deg[i][0,0],s_mag[i][1,0],s_deg[i][1,0],s_mag[i][0,1],s_deg[i][0,1],s_mag[i][1,1],s_deg[i][1,1]] for i in range(len(freq))])
    return res

    