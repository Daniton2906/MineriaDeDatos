import pyreclab
from random import *

def show_lines(filename):
    with open(filename) as infile:
        for line in infile:
            print(line)

def get_customer_evaluations(filename, output, header, max_id=17770):
    fd = open(output, "w")
    if header:
        fd.write("user_id\tmovie_id\trating\n")
    movie_id = 0; customer_array = []
    with open(filename) as infile:
        for line in infile:
            if movie_id == 0:
                movie_id = line.split(":", 1)[0]
            else:
                customer_array.append(line[:-1].split(",")[1])

    n = 0
    for i in range(1, max_id+1):
        print "Revisando movie"+str(i)+".txt"
        movie_id = 0; lines_array = []
        with open(url+ "movies/movie" + str(i) + ".txt") as infile:
            for line in infile:
                if movie_id == 0:
                    movie_id = line.split(":", 1)[0]
                else:
                    aux = line[:-1].split(",")
                    try:
                        j = customer_array.index(aux[0])
                    except ValueError:
                        j = -1
                    if j != -1:
                        n += 1
                        fd.write(str(j) + "\t" + movie_id + "\t" + aux[1] + "\n")
    fd.close()
    return n

def create_training_and_probe_set(filename, file_size, output_training, output_probe, probe_size, header):
    fd_1 = open(output_training, "w")
    fd_2 = open(output_probe, "w")
    probe_lines = []; training_lines = range(0, file_size)
    seed()
    for _ in range(0, probe_size):
        i = training_lines[randint(0, len(training_lines))]
        probe_lines.append(i); training_lines.remove(i)
    probe_lines.sort()
    #print len(probe_lines)
    counter = 0; actual_line = 0
    with open(filename) as infile:
        for line in infile:
            #print line
            if header:
                header = False; continue
            elif counter < probe_size and probe_lines[counter] == actual_line:
                fd_2.write(line) #escribir en probe dataset
                counter += 1
            else:
                fd_1.write(line) #escribir en training dataset
            actual_line += 1
    fd_1.close(); fd_2.close()
    return probe_size

def sort_csv(filename, output):
    lines = []
    with open(filename) as infile:
        for line in infile:
            lines.append(line)

    lines.sort(lambda a, b: int(a[:-1].split(",")[1]) - int(b[:-1].split(",")[1]))
    fd = open(output, 'w')
    for line in lines:
        fd.write(line)
    fd.close()

import os.path

data_chunks = 5

url = r'/home/ddiomedi/Desktop/mineria/exploracion_de_datos/netflix-prize-data/'
data_url = r'/home/ddiomedi/Desktop/mineria/new_data/'

data_filename = url+'mydata' #5.csv'
rating_filename = data_url+'ratings' #5" + ".txt"
training_filename = data_url+"training"
probe_filename = data_url+"probe"
size_filename = data_url+'size.txt' #5" + ".txt"


if not os.path.isfile(size_filename):
    fs = open(size_filename, 'w')
else:
    fs = open(size_filename, 'r')

size_list = range(data_chunks)
for i in range(data_chunks):
    size_list[i] = -1

for i in range(1, data_chunks + 1):
    f_in = data_filename + str(i) +'.csv'
    f_r = rating_filename + str(i) + ".txt"
    if not os.path.isfile(f_r):
        print "Extrayendo evaluaciones de",f_in,"..."
        size_list[i-1] = get_customer_evaluations(f_in, f_r, False, 1000)
        fs.write(str(size_list[i-1])+'\n')
        print "Obtenidas",size_list[i-1],"evaluaciones."
    else:
        size_list[i-1] = int(fs.readline()[:-1])
        print "Archivo ya creado:",size_list[i-1],"evaluaciones."
    f_t = training_filename + str(i) + ".txt"
    f_p = probe_filename + str(i) + ".txt"
    if not os.path.isfile(f_t):
        print "Creando set de entrenamiento y de prueba", i, "..."
        create_training_and_probe_set(f_r, size_list[i-1], f_t, f_p, 10000, False)
        print "Tamano probe set:",10000
