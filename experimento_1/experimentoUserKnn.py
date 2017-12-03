import pyreclab
from random import *
from exp_base import *
import os.path

#########################################################################################################
######                              UserKnn                                                        ######
#########################################################################################################

prediction_filename = data_url+'predictionsUserKnn' #5.csv'
ordenada_filename = data_url+'ordenadasUserKnn' #5.csv'

print 'UserKnn'
for i in range(1, data_chunks + 1):
    f_t = training_filename + str(i) + ".txt"
    f_p = probe_filename + str(i) + ".txt"
    f_pred = prediction_filename + str(i) + ".csv"
    f_ord = ordenada_filename + str(i) + ".csv"

    print "Corriendo experimento ", i, "..."
    print 'Entrenando...'
    obj = pyreclab.UserKnn( dataset = f_t,
                               dlmchar = b'\t',
                               header = True,
                               usercol = 0,
                               itemcol = 1,
                               ratingcol = 2 )
    obj.train(10, 'pearson')
    print 'Prediciendo...'
    #prediction = obj.predict( "630685", "1")
    #ranking = obj.recommend( "630685", 10, True)
    #print prediction
    #print ranking

    predictionList, mae, rmse = obj.test( input_file = f_p,
                                              dlmchar = b'\t',
                                              header = False,
                                              usercol = 0,
                                              itemcol = 1,
                                              ratingcol = 2,
                                              output_file = f_pred)

    print "mae=",mae
    print "rmse=",rmse
    print 'Ordenando...'
    sort_csv(f_pred, f_ord)
