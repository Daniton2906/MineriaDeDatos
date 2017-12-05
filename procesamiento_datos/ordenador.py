#Dado que se tenia un archivo de texto por pelicula en donde cada linea era una reseña
#Se decidio ordenarlo de forma de tener un gran texto con el nombre de la pelicula junto a su reseña
#Y no las reseñas sin peliculas
import os.path

output = open("output.txt", "a")

#Se tomaron las primeras 1000 peliculas
for i in range(1000):
    directorio = "movie" + str(i+1) + ".txt"
    if os.path.isfile(directorio):
        pelicula = open(directorio, "r")

        j = 0
        for line in pelicula:
            if j == 0:
            	#String con el nombre de la pelicula
                nombre_pelicula = line[:-3]
                j+=1
            else:
            	#line en este caso es la reseña, lo que se adjunta con el nombre del filme
                nueva_linea = nombre_pelicula + "," + line
                output.write(nueva_linea)
        
        pelicula.close()

output.close()
