#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Esquema de columnas del documento CSV.
#columns = ["estacion","m/s vento a 10m","Refacho a 10m (m/s)","(m/s)","Refacho a 30m (m/s)", "Desviación típica da velocidade do vento a 30m (m/s)","Desviación típica da velocidade do vento a 10m (m/s)","Desviación típica da dirección do vento a 10m (grados)","Desviación típica da dirección do vento a 30m (grados)","Dirección do refacho a 30m (grados)","Dirección do vento a 30m (grados)","Dirección do refacho a 10m (grados)","Dirección do vento a 10m (grados)","Temperatura a 1.5m (grados C)","Temperatura a 0.1m (grados C)","Temperatura a 30m (grados C)","Temperatura a 10m (grados C)","Humidade Relativa a 10m (%)","Humidade Relativa a 1.5m (%)","Radiación solar W/m2,Radiación difusa W/m2","Chuvia L/m2,Presión hPa","Horas de sol","Temperatura de orballo a 1.5m ºC","Temperatura do chan a -0.5m ºC","Temperatura do chan a -0.1m ºC/26/_Valor","Presión reducida hPa",_"Data"]

# Crear dataframe from csv.
df = pd.read_csv('Dataset/estacion-ok.csv', sep=',',header=0)

# Imprimir por columna.
print(df.head()['estacion'])
print(df.head()['Horas de sol'])


