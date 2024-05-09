#   Ejemplo viga

from openseespy.opensees import *
import openseespy.opensees as ops
import numpy as np
import matplotlib.pyplot as plt
# from openseespy.postprocessing.Get_Rendering import *

wipe()

#   1.0 Definicnion del modelo

model('basic','-ndm',2,'-ndf',3)

#   2.0 Coordenadas de los nodos

L=1.0

ops.node(1, 0.0, 0.0)
node(2, 1*L, 0.0)
node(3, 2*L, 0.0)
node(4, 3*L, 0.0)

#   3.0 Condiciones de apoyo

fix(1, 1, 1, 0)
fix(2 ,0, 1, 0)
fix(3, 0, 1, 0)
fix(4, 0, 1, 0)

#   4.0 Definición de los elementos

geomTransf('Linear',1)

A=1.0
E=1.0
I=1.0

element('elasticBeamColumn',1,1,2,A,E,I,1)
element('elasticBeamColumn',2,2,3,A,E,I,1)
element('elasticBeamColumn',3,3,4,A,E,I,1)

#   5.0 Cargas

w=1.0

timeSeries('Constant',1)
pattern('Plain',1,1)

eleLoad('-ele',1,'-type','-beamUniform',-w)
eleLoad('-ele',2,'-type','-beamUniform',-w)

#   6.0 Analisis

analysis('Static')
analyze(1)

#   7.0 Resultados

reactions()
print(nodeReaction(1))
print(nodeReaction(2))
print(nodeReaction(3))
print(nodeReaction(4))

#   8.0 Fuerzas en los extremos de los elementos
print(eleForce(1))
print(eleForce(2))
print(eleForce(3))
print(eleForce(4))#   Ejemplo viga




# import OpenSeesPy rendering module
import openseespy.postprocessing.Get_Rendering as opsplt

# render the model after defining all the nodes and elements
opsplt.plot_model()

# plot mode shape
#opsplt.plot_modeshape(3)