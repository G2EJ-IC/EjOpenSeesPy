# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:41:13 2021

@author: IC.EJGuerreroG
"""

import pandas as pd
import numpy as np

"""
K = np.array([[144, -48, 0],
              [-48, 72,-24],
              [0, -24, 24]])

M = np.array([[24, 0, 0],
              [0, 24, 0],
              [0, 0, 18]])
"""

excel_file = 'EjemploMatrixPy.xlsx'

K = pd.read_excel(excel_file , sheet_name = 'K', index_col=None).to_numpy()

M = pd.read_excel(excel_file , sheet_name = 'M', index_col=None).to_numpy()

print('\n\nK =\n', K)

print('\n\nM =\n', M)

f = np.linalg.inv(K)

print ('\n\nf =', f)

D = np.dot(f,M)

print ('\n\nD =\n', D)

Valores, Vectores = np.linalg.eig(D)

print('\n\nValores =\n', Valores)

print ('\n\nVectores =\n', Vectores)