import os

path = 'C:\\Users\\Skayd\\PycharmProjects\\Schule\\SRC\\Aufgabe 18'
lst = os.listdir(path)

for p in lst:
    print(p)
    #lst2 = os.listdir(path)
    #for f in lst2:
    lineNr = 0
    with open(path + '\\' + p, "r") as reader:
        #print(f)
        line = reader.readline()
        while line != '':
            #print(str(lineNr) + "\t" + line)
            line =reader.readline()
            lineNr +=1
        print('Dateiname: ' + p + 'Anzahl der Zeihlen: ' + str(lineNr))