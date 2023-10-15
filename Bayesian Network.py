import bnlearn as bn
import pandas

###### PARTE 1.1 ######
data = pandas.read_csv('dataset18-1.csv')
modelo = bn.structure_learning.fit(data) #Dada una muestra de datos, estima un DAG que captura las dependencias entre las variables.
plotz = bn.plot(modelo)

###### PARTE 1.2 ######
modelo = bn.parameter_learning.fit(modelo,data) #
query = bn.inference.fit(modelo, variables=['precios_altos'], evidence={'guerra_ucrania':1, 'inflacion':1}) #Consulta probabilidades de precios_altos 0|1 -> guerra_ucrania(1) & inflacion(1)
#plotz = bn.plot(modelo)
query = bn.inference.fit(modelo, variables=['guerra_ucrania'], evidence={'escasez':0, 'inflacion':0}) #Consulta probabilidades de guerra_ucrania 0|1 -> escasez(0) & inflacion(0)
#plotz = bn.plot(modelo)
query = bn.inference.fit(modelo, variables=['no_alcohol'], evidence={'escasez':0, 'precios_altos':1}) #Consulta probabilidades de no_alcohol 0|1 -> escasez(0) & precios_altos(1)
#plotz = bn.plot(modelo)

