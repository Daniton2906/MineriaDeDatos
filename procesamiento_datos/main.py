from procesador import *
from compare import *

#process_combined_data(url)
#fix_movie_file("movies/movie1.txt", compare_dates)

print("Calculando cantidad de evaluaciones por pelicula")
dict1 = {'fun': cantidad, 'valor_inicial': 0, 'output_name': url+"movie_amount_ratings", 'column_name': "evaluaciones_recibidas"}
n1 = reduce_movie_files(url+"movies/movie", dict1)

print("Calculando promedios de evaluaciones por pelicula")
dict2 = {'fun': average, 'valor_inicial': 0, 'output_name': url+"movie_average_ratings", 'column_name': "rating_promedio"}
n2 = reduce_movie_files(url+"movies/movie", dict2)

print("Calculando cantidad de evaluaciones por cliente")
dict4 = {'compare': compare_id, 'output_name': url+"customers", 'column_name': "evaluaciones_hechas"}
n4 = make_customer_file(url+"movies/movie", dict4)

#show_lines(dict4['output_name']+".csv")
print("Total evaluaciones hechas: " + str(reduce_file(dict4['output_name']+".csv", lambda x, y: y + int(x[:-1].split(",")[1]), 0)))

print("Arreglando movie_titles.csv")
dict5 = {'output_name': url+"fixed_movie_titles", 'column_name': "id,anho_de_lanzamiento,titulo"}
fix_movie_titles(url+"movie_titles.csv", dict5)

'''
print("Juntando todas las evaluaciones en un csv")
dict6 = {'output_name': url+"all_ratings", 'column_name': "customerID,rating,date"}
create_super_file(url+"movies/movie", dict6)
'''
