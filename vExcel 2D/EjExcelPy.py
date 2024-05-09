# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 23:06:41 2021

@author: IC.EJGuerreroG
"""

#Change plot backend to Qt. ONLY if you are using an Ipython console (e.g. Spyder)
#%matplotlib qt

#Change plot backend to 'Nbagg' if using in Jupyter notebook to get an interactive, inline plot.
#%matplotlib notebook

import sys
#sys.path.append('C:/ProgramData/Anaconda3/Lib/site-packages/openseespywin')

from openseespy.opensees import *
#import openseespy.postprocessing.Get_Rendering as opsplt
import openseespyvis.Get_Rendering as opsplt
import openseespy.opensees as ops
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import openseespy.postprocessing.Get_Rendering as opsplt
#import openseespy.postprocessing as opsplt
#from openseespy.postprocessing.Get_Rendering import *

ops.wipe()

#Importar Libro de Excel

E = 29500.0
massX = 0.49
M = 0.
coordTransfV = 'Linear'  # Linear, PDelta, Corotational
coordTransfC = 'PDelta'  # Linear, PDelta, Corotational
massType = "-lMass"  # -lMass, -cMass
excel_file = 'EjemploPy v001.xlsx'
nodos = pd.read_excel(excel_file , sheet_name = 'pNodos').to_numpy()
elementos = pd.read_excel(excel_file , sheet_name = 'pElementos').to_numpy()

#   1.0 Definicnion del modelo
#model( 'básico' , '-ndm' , ndm , '-ndf' , ndf = ndm * (ndm + 1) / 2 )

#model('basic','-ndm',2)
model('basic','-ndm',2,'-ndf',3)

#   2.0 Coordenadas de los nodos
#node( nodeTag , * crds , '-ndf' , ndf , '-mass' , * mass , '-disp' , * disp , '-vel' , * vel , '-accel' , * accel )

for i in range (len(nodos)):
    nodeTag =int(nodos[i,0])
    CoorX = float(nodos[i,1])
    CoorY = float(nodos[i,2])
    ops.node(nodeTag, CoorX, CoorY)
    if i<=3:
        #   3.0 Condiciones de apoyo        
        ops.fix(nodeTag, 1, 1, 1)
opsplt.plot_model('nodes')

#   4.0 Definición de los elementos

# add column element
#element( 'elasticBeamColumn' , eleTag , * eleNodes , Area , E_mod , Iz , transfTag , <'- mass' , mass> , <'- cMass'> , <'- release' , releaseCode> )
#Vigas
ops.geomTransf(coordTransfV, 1)
#Columnas
ops.geomTransf(coordTransfC, 2)

A=1.0
E=1.0
I=1.0
transfTag=1

for i in range (len(elementos)):
    eleTag =int(elementos[i,0])
    NudoI = int(elementos[i,1])
    NudoJ = int(elementos[i,2])
    ops.element('elasticBeamColumn',eleTag,NudoI,NudoJ,A,E,I,transfTag)
opsplt.plot_model('nodes' , 'elements')

# render the model after defining all the nodes and elements


ops.wipe()