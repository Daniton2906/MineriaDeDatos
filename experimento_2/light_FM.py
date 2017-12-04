import numpy as np
from scipy.sparse import csr_matrix
from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from lightfm.evaluation import auc_score

dic = {}


def movie_data(file, matrix, movie):
    global dic
    print(movie)
    for line in file:
        costumer = line.split(',')
        try:
            matrix[movie, dic[costumer[0]]] = int(costumer[1])
        except KeyError:
            pass


def parse_data():
    global dic
    file = open("mydata3.txt", 'r')
    i = 0
    for line in file:
        a = line.split('\t')
        dic[a[0]] = i
        i += 1
    matrix = csr_matrix((17770, i), dtype=np.float32)
    for movie in range(100):
        movie_file = open("movie" + str(movie + 1) + ".txt", 'r')
        movie_file.readline()
        movie_data(movie_file, matrix, movie)
        movie_file.close()
    file.close()
    return matrix


z = parse_data()
train = z[0:49, 0:]
test = z[50:99, 0:]


def experiment(type_exp):
    global train, test
    model = LightFM(learning_rate=0.05, loss=type_exp)
    model.fit(train, epochs=10)

    train_precision = precision_at_k(model, train, k=10).mean()
    test_precision = precision_at_k(model, test, k=10).mean()

    train_auc = auc_score(model, train).mean()
    test_auc = auc_score(model, test).mean()

    output = open("mid100mostRaiting5.txt", 'w')
    output.write("La presicion del training set es: " + str(train_precision) + "\n")
    output.write("La presicion del test set es: " + str(test_precision) + "\n")
    output.write("El auc del training set es: " + str(train_auc) + "\n")
    output.write("El auc del test set es: " + str(test_auc) + "\n")
    output.close()

print("inicio")
#test1()
experiment('bpr')
#experiment('wrap')
print("termino")


def test1():
    d = csr_matrix((3, 5), dtype=np.float32)
    d[0, 0] = 9
    d[1, 4] = 8
    print(d.toarray())

