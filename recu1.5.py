"""Estamos fuera de la función, importando la librería csv. """

import csv #importación de la librería estándar.


def process_class():
  """ ya dentro de la funcion principal, con, con sus interaciones de un tabulador"""
   
  Lista_de_diccionarios = []  #aqui es la litas que almacenamos.
  """ Estamos leyendo el fichero"""

  """ Almacenar los nombres de las claves que están en la cabecera del archivo"""
  with open("class.csv",'r') as file:
    primera_linea = file.readline()
    claves = primera_linea.split(",")  # Leer la primera línea de cabecera, que son las claves
                                                    # de la lista de diccionario.

  with open("class.csv",'r') as file:  # Abrimos el archivo en modo lectura
    archivo = file.readlines()[1:]  # Saltamos la primera línea de cabecera
    
  """pasamos a la interacción  del documento"""
  for fila in archivo: # interacción de cada fila del documento.
   #agregamos nombre y apellido del alumno a nuestra lista con Append
    Lista_de_diccionarios.append(dict(zip(claves, fila.split(",")))) #agregamos nombre y apellido del alumno a nuestra lista con Append
   
 
  print(Lista_de_diccionarios) #imprime  la lista del deccionaario al hacer el llamamiento a la funcion.


process_class() #LLAMAMIENTO DE LA FUNCION PRINCIPAL.



