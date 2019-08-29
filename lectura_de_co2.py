# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:26:28 2019

"""

from xml.dom import minidom
import csv
import pandas as pd

doc = minidom.parse("D:\Proyectos\Sumo\Simulacion\emisiones.xml")
tiempo = doc.getElementsByTagName("timestep")
contTiempo =0
sumaTiempo =0.0
emisionCO2 = []
emisionCO = []
emisionHC = []
emisionNox = []
emisionPmx = []
emisionfuel = []
time=[]
for i in tiempo:
    timeaux = float(i.getAttribute("time")) 
    time.append(timeaux)
    vehiculo = i.getElementsByTagName("vehicle")
    cont =0
    sumaCO2 =0.0
    sumaCO =0.0
    sumaHC =0.0
    sumaNOx =0.0
    sumaPmx =0.0
    sumafuel =0.0
    for j in vehiculo:
        sumaCO2 += float(j.getAttribute("CO2"))
        sumaCO += float(j.getAttribute("CO"))
        sumaHC += float(j.getAttribute("HC"))
        sumaNOx += float(j.getAttribute("NOx"))
        sumaPmx += float(j.getAttribute("PMx"))
        sumafuel  += float(j.getAttribute("fuel"))
        cont +=1
    print("entreeeeee")
    emisionCO2.append(sumaCO2/cont)
    emisionCO.append(sumaCO/cont)
    emisionHC.append(sumaHC/cont) 
    emisionNox.append(sumaNOx/cont)
    emisionPmx.append(sumaPmx/cont)
    emisionfuel.append(sumafuel/cont)

data = {"tiempo":time,"Emision CO2":emisionCO2,"Emision CO":emisionCO,"Emision HC":emisionHC,"Emision Nox":emisionNox,"Emision Pmx":emisionPmx,"Emision fuel":emisionfuel}
df = pd.DataFrame(data, columns = ["tiempo", "Emision CO2", "Emision CO", "Emision HC", "Emision Nox","Emision Pmx","Emision fuel"])
df.to_csv('D:\Proyectos\Sumo\Simulacion\datosEmisiones.csv')

       






