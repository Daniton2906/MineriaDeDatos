'''
procesador.py

Separamos los datos de los archivos combined_data para
hacer un archivo para cada pelicula con todas las evaluaciones recibidas

Hecho por Daniel Diomedi, 2017-09-29
'''

from compare import *
from Printer import Printer
from My_Array import MyArrayList

temp_name = "movies/movie"
url = r'/home/ddiomedi/Desktop/mineria/exploracion_de_datos/netflix-prize-data/'
#url = r'C:/Users/Daniel/Desktop/Semestre2017-2/Introduccion a la Mineria de Datos/netflix-prize-data/'
global fd, contador


def reduce_file(filename, fun, init_value):
    n = init_value
    skip_first = True
    with open(filename) as infile:
        for line in infile:
            if skip_first:
                skip_first = False
                continue
            else:
                n = fun(line, n)
    return n


def show_lines(filename):
    with open(filename) as infile:
        for line in infile:
            print(line)

# separate_movies: str -> int
# lee un archivo tipo "combined_data" para separar cada
# pelicula en diferentes archivos con todos sus ratings
# Retorna la cantidad de archivos creados
def separate_movies(filename):
    global fd, contador
    contador += 1
    first_movie = True
    with open(filename) as infile:
        for line in infile:
            if ':' in line:
                if not first_movie:
                    contador += 1
                    fd.close()
                else:
                    first_movie = False
                fd = open(temp_name + str(contador) + ".txt", "w")
                # print "crear archivo para movie",contador
            fd.write(line)
    return contador


# process_combined_data: None -> None
# Procesa todos los archivos tipo "combined_data"
def process_combined_data(url):
    global contador
    print("Procesando todos los datos")
    contador = 0
    filename1 = url+"combined_data_1.txt"
    cuenta1 = separate_movies(filename1)
    print "Salieron", cuenta1, "lineas de", filename1

    filename2 = url+"combined_data_2.txt"
    cuenta2 = separate_movies(filename2) - cuenta1
    print "Salieron", cuenta2, "lineas de", filename2

    filename3 = url+"combined_data_3.txt"
    cuenta3 = separate_movies(filename3) - cuenta2 - cuenta1
    print "Salieron", cuenta3, "lineas de", filename3

    filename4 = url+"combined_data_4.txt"
    cuenta4 = separate_movies(filename4) - cuenta3 - cuenta2 - cuenta1
    print "Salieron", cuenta4, "lineas de", filename4

    print "Final:", contador, "lineas."


# print_array(): array -> None
# imprimer arreglo linea por linea
def print_array(array):
    for line in array:
        print line


def fix_movie_file(filename, compare=None):
    movie_id = 0
    lines_array = []
    with open(filename) as infile:
        for line in infile:
            if movie_id == 0:
                movie_id = line.split(":", 1)[0]
            else:
                lines_array.append(line[:-1].split(","))

    if compare is not None:
        lines_array.sort(compare)
        #sorted(lines_array, key=cmp_to_key(compare))

    fd = open("movie" + str(movie_id) + "_fixed.csv", "w")
    fd.write("customerid,rating,date\n")
    for element in lines_array:
        fd.write(element[0] + "," + element[1] + "," + element[2] + "\n")
    fd.close()
    print_array(lines_array)
    return len(lines_array) + 1

#
#
def reduce_movie_files(filename, d, max_id=17770):
    m = Printer(max_id)
    fd = open(d['output_name'] + ".csv", "w")
    fd.write("movieid," + d['column_name'] + "\n")

    for i in range(1, max_id + 1):
        m.update()
        movie_id = 0; lines_array = []
        with open(filename + str(i) + ".txt") as infile:
            for line in infile:
                if movie_id == 0:
                    movie_id = line.split(":", 1)[0]
                else:
                    lines_array.append(line[:-1].split(","))

        fun = d['fun']; n = None
        if fun is not None:
            n = fun(lines_array, d['valor_inicial'])

        fd.write(str(movie_id) + "," + str(n) + "\n")

    m.close()
    fd.close()

# make_customer_file: str dict int -> None
# Crear archivo con la cantidad de evaluaciones que hizo cada cliente
def make_customer_file(filename, d, max_id=17770):
    print "Leyendo archivos movie"
    m = Printer(max_id)
    new_filename = d['output_name'] + ".csv"
    fd = open(new_filename, "w")
    fd.write("customerid," + d['column_name'] + "\n")

    customer_array = MyArrayList()
    for i in range(1, max_id + 1):
        m.update()
        with open(filename + str(i) + ".txt") as infile:
            for line in infile:
                if ':' in line:
                    continue
                else:
                    customer_array.insert(line[:-1].split(","))

    m.close()
    print "Creando archivo " + new_filename
    m.reset(customer_array.get_length())

    compare = d['compare']
    customer_array.sort(compare)
    for i in range(0, customer_array.get_length()):
        m.update()
        fd.write(customer_array.toLine(i))

    m.close()
    fd.close()
    return customer_array.get_length() + 1

def fix_movie_titles(filename, d):
    print "Leyendo archivo " + filename
    n = numero_lineas(filename)
    new_filename = d['output_name'] + ".csv"
    fd = open(new_filename, "w")
    fd.write(d['column_name'] + "\n")
    print "Creando archivo " + new_filename
    m = Printer(n)
    with open(filename) as infile:
        for line in infile:
            m.update()
            fd.write(line)

    m.close()
    fd.close()
    return n + 1


def numero_lineas(filename):
    return reduce_file(filename, lambda x, y: y + 1,0)

def cantidad(array, n):
    for _ in array:
        n += 1
    return n

def average(array, n):
    for i in array:
        n += int(i[1])
    return round(n/max(1, len(array)), 3)


'''
import sys
import time

a = 0
for x in range (0,3):
    a = a + 1
    b = ("Loading" + "." * a)
    # \r prints a carriage return first, so `b` is printed on top of the previous line.
    sys.stdout.write('\r'+b)
    time.sleep(0.5)
print (a)
'''


#
#
def create_super_file(filename, d, max_id=17770):
    m = Printer(max_id)
    fd = open(d['output_name'] + ".csv", "w")
    fd.write("movieid," + d['column_name'] + "\n")

    for i in range(1, max_id + 1):
        m.update()
        movie_id = 0; lines_array = []
        with open(filename + str(i) + ".txt") as infile:
            for line in infile:
                if movie_id == 0:
                    movie_id = line.split(":", 1)[0]
                else:
                    fd.write(str(movie_id) + "," + line)

    m.close()
    fd.close()
