

data_url = r'/home/ddiomedi/Desktop/mineria/new_data/'
probe_filename = data_url+"probe"

p1 = 'ordenadasUserAvg' #5.csv'

p2 = 'ordenadasUserKnn' #5.csv'

p3 = 'ordenadasItemKnn' #5.csv'

p4 = 'ordenadasSVD' #5.csv'

for p in [p3, p4]:
    for i in [1,5]:#range(1, 6):
        counter = 0
        with open(data_url + p + str(i) + ".csv") as pred:
            with open(probe_filename + str(i) + ".txt") as probe:
                for j in range(100):
                    r_pred = pred.readline()[:-1].split(",")
                    r_probe = probe.readline()[:-1].split("\t")
                    if int(round(float(r_pred[2]))) == int(r_probe[2]):
                        counter += 1
                        #print r_pred[1],":", int(round(float(r_pred[2])))
                        #print r_probe[1],":", int(r_probe[2])
        print p + str(i) + ".csv --> " + str(counter) + " aciertos."

#print int(round(4.5))
#print int(round(4.45))
#print int(round(4.55))
