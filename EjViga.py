#   Ejemplo viga

import openseespy.opensees as ops
import numpy as np
import matplotlib.pyplot as plt

from openseespy.postprocessing.Get_Rendering import *

ops.wipe()

#   1.0 Definicnion del modelo

ops.model('basic','-ndm',2,'-ndf',3)

#   2.0 Coordenadas de los nodos

L=1.0

ops.node(1, 0.0, 0.0)
ops.node(2, 1*L, 0.0)
ops.node(3, 2*L, 0.0)
ops.node(4, 3*L, 0.0)

#   3.0 Condiciones de apoyo

ops.fix(1, 1, 1, 0)
ops.fix(2 ,0, 1, 0)
ops.fix(3, 0, 1, 0)
ops.fix(4, 0, 1, 0)

#   4.0 Definición de los elementos

ops.geomTransf('Linear',1)

A=1.0
E=1.0
I=1.0

ops.element('elasticBeamColumn',1,1,2,A,E,I,1)
ops.element('elasticBeamColumn',2,2,3,A,E,I,1)
ops.element('elasticBeamColumn',3,3,4,A,E,I,1)

#   5.0 Cargas

w=1.0

ops.timeSeries('Constant',1)
ops.pattern('Plain',1,1)

ops.eleLoad('-ele',1,'-type','-beamUniform',-w)
ops.eleLoad('-ele',2,'-type','-beamUniform',-w)

#   6.0 Analisis

ops.analysis('Static')
ops.analyze(1)

#   7.0 Resultados

ops.reactions()
print(ops.nodeReaction(1))
print(ops.nodeReaction(2))
print(ops.nodeReaction(3))
print(ops.nodeReaction(4))

#   8.0 Fuerzas en los extremos de los elementos
print(ops.eleForce(1))
print(ops.eleForce(2))
print(ops.eleForce(3))
print(ops.eleForce(4))#   Ejemplo viga

# import OpenSeesPy rendering module
import openseespy.postprocessing.Get_Rendering as opsplt

# render the model after defining all the nodes and elements
opsplt.plot_model()

# plot mode shape
#opsplt.plot_modeshape(3)
