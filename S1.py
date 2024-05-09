# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#wipe()

from openseespy.opensees import *
#import openseespy.opensees as ops
import numpy as np
import matplotlib.pyplot as plt

#ops.clear
wipe()

###Dimensiones del modelo
model('basic','-ndm',2,'-ndf',3)

###Coordenadas de los nodos
L=1.0
node(1, 0.0, 0.0)
node(2, L, 0.0)
node(3, 2*L, 0.0)
node(4, 3*L, 0.0)


###condiciones de apoyo
# nodo, UX, UY, RZ
fix(1,1,1,0)
fix(2,0,1,0)
fix(3,0,1,0)
fix(4,0,1,0)

###Elementos
geomTransf('Linear', 1)
Area=1.0
E_mod=1.0
Iz=1.0
#element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, Iz, transfTag, <'-mass', mass>, <'-cMass'>, <'-release', releaseCode>)
##Para modelos de 2D
#element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag, <'-mass', mass>, <'-cMass'>)
element('elasticBeamColumn', 1, 1, 2, Area, E_mod, Iz, 1)
element('elasticBeamColumn', 2, 2, 3, Area, E_mod, Iz, 1)
element('elasticBeamColumn', 3, 3, 4, Area, E_mod, Iz, 1)

##ops.element('ModElasticBeam2d', eleTag, *eleNodes, Area, E_mod, Iz, K11, K33, K44, transfTag, <'-mass', massDens>, <'-cMass'>)
#ops.element('ModElasticBeam2d', eleTag, *eleNodes, Area, E_mod, Iz, 1)

###Cargas
W=1.0
timeSeries('Constant', 1)
pattern('Plain', 1, 1)
eleLoad('-ele', 1, '-type', '-beamUniform', -W)
eleLoad('-ele', 2, '-type', '-beamUniform', -W)


###Analisis
analysis('Static')
ok = analyze(1)
if ok==0:
    print('Análisis Exitoso')
else:
    print('Error')
    
###Resultados    
reactions()
print(nodeReaction(1))
print(nodeReaction(2))
print(nodeReaction(3))
print(nodeReaction(4))




# import OpenSeesPy rendering module
import openseespy.postprocessing.Get_Rendering as opsplt

# render the model after defining all the nodes and elements
opsplt.plot_model()

# plot mode shape
#opsplt.plot_modeshape(3)