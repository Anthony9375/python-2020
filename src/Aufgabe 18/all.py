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

filePath= 'C:\\Users\\Skayd\\PycharmProjects\\Schule\\SRC\\Aufgabe 18'
with open(filePath, 'r') as reader:
    print(reader.read())

with open(filePath, 'r') as reader:
    lst = reader.readlines()
    print("Zeile 4: " + lst[4])

lineNr = 0
with open(filePath, 'r') as reader:
   line = reader.readline()
   while line != '':  # The EOF char is an empty string
      print(str(lineNr) + "\t" + line)
      line = reader.readline()
      lineNr +=1

filePath= 'C:\\Users\\Skayd\\PycharmProjects\\Schule\\SRC\\Aufgabe 18'

msg = "class Kreis"
with open(filePath, 'w') as writer:
    writer.write(msg)

with open(filePath, 'a') as a_writer:
    a_writer.write('\nmsg')

filePath_source= 'C:\\Users\\Skayd\\PycharmProjects\\Schule\\SRC\\Aufgabe 18'
filePath_destination = 'C:\\Users\\Skayd\\PycharmProjects\\Schule\\SRC\\Aufgabe 18'

with open(filePath_source, 'r') as source_reader, open(filePath_destination, 'w') as destination_writer:
   source_content = source_reader.readlines()
   destination_writer.writelines(reversed(source_content))