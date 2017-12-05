#Porgrama genera la matriz en donde las filas son los usuarios, las columnas son las peliculas y las celdas
#Si el usuario califico a la pelicula con una nota mayor a 3
import os.path

peliculas = open("output.txt", "r")
output = open("output_peliculas.txt", "a")

#Se definen los titulos de las peliculas por ids
for i in range(1000):
    output.write(i+1)

d = {}

#Se defne un diccionario con los usuarios
for movie in peliculas:
    datos = movie.split(",")
    usuario = datos[1]
    d[usario] = []

#A cada arreglo respectivo de un usuario se le agrega las peliculas que ha calificado con nota mayor a 3
for movie in peliculas:
    datos = movie.split(",")
    nombre = datos[0]
    usuario = datos[1]
    calificacion = datos[2]
    fecha = datos[3]
    if calificacion > 3:
        d[usario].append(nombre)

#Se itera sobre los usuarios y se agrega a la matriz el valor de 1 o 0 dependiendo si vieron o no la pelicula
for usuario in d:
    for i in range(1000):
        if (i+1) in d[usuario]:
            output.write(1):
        else:
            output.write(0)

output.close()
