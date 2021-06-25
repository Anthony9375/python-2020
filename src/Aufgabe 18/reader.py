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